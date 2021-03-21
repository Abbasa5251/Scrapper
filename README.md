# **StackoverFlow Scrapper**

## **Getting Started**

### Install required Modules

```bash
pipenv install
```

### Activate _virtual environment_

```bash
pipenv shell
```

### Scrapping Stack Overflow

```python
scrape_tag() # returns List of data
```

#### Parameters

```python
scrape_tag(
    tag=[optional, default="Python"],
    query_filter=[optional, default="Views"],
    max_pages=[optional, default=50],
    page_size=[optional, default=25]
)
```
