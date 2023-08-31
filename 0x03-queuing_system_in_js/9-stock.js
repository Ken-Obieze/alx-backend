import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

const getItemById = (id) => listProducts.find(item => item.itemId === id);

const reserveStockById = async (itemId, stock) => {
  await client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return parseInt(reservedStock, 10) || 0;
};

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.initialAvailableQuantity - reservedStock;

  res.json({ ...item, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.initialAvailableQuantity - reservedStock;

  if (currentQuantity <= 0) {
    res.json({ status: 'Not enough stock available', itemId });
  } else {
    await reserveStockById(itemId, reservedStock + 1);
    res.json({ status: 'Reservation confirmed', itemId });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
