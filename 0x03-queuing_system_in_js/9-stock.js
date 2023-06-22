const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

const getItemById = (id) => {
  return listProducts.find(item => item.id === id);
};

const app = express();
const port = 1245;

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

const redisClient = redis.createClient();
const hgetAsync = promisify(redisClient.hget).bind(redisClient);
const hsetAsync = promisify(redisClient.hset).bind(redisClient);

const reserveStockById = async (itemId, stock) => {
  await hsetAsync('item', itemId, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await hgetAsync('item', itemId);
  return reservedStock ? parseInt(reservedStock) : 0;
};

app.get('/list_products', (req, res) => {
  const products = listProducts.map(item => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  }));
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: item.stock - currentStock
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock >= item.stock) {
    res.json({ status: 'Not enough stock available', itemId: item.id });
  } else {
    await reserveStockById(itemId, currentStock + 1);
    res.json({ status: 'Reservation confirmed', itemId: item.id });
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
