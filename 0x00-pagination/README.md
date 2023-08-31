# Pagination

# Deletion-Resilient Hypermedia Pagination

This project implements deletion-resilient hypermedia pagination for a database of popular baby names. It provides a Server class that allows paginating through the dataset while accounting for potential deletions of rows between queries.

## Requirements

- Python 3.x
- `csv` module

## Usage

1. Clone the repository:

   git clone https://github.com/your-username/alx-backend/0x00-pagination

2. Import the Server class in your Python script:
from server import Server

3. Create an instance of the Server class:
server = Server()

4. Paginate through the dataset:
page = server.get_page(page=2, page_size=20)
print(page)

This will retrieve the second page with a page size of 20. If any rows were deleted from the dataset between queries, the pagination will adjust accordingly.

API Reference
`Server` Class
`get_page(page: int = 1, page_size: int = 10) -> List[List]`
Returns the corresponding page of the dataset for the given pagination parameters.

* page: The page number (default: 1)
* page_size: The number of rows per page (default: 10)
Returns:

A list of rows representing the dataset page.
get_hyper(page: int = 1, page_size: int = 10) -> dict
Returns a dictionary containing the pagination information for the given parameters.

* page: The page number (default: 1)
* page_size: The number of rows per page (default: 10)
* Returns:

* A dictionary with the following key-value pairs:
	* "page_size": The length of the returned dataset page.
	* "page": The current page number.
	* "data": The dataset page.
	* "next_page": The number of the next page (or None if there is no next page).
	* "prev_page": The number of the previous page (or None if there is no previous page).
	* "total_pages": The total number of pages in the dataset.
