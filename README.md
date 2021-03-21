# **StackOverflow Scrapper**

## **Getting Started**

### Installing Python Virtualenv

```ps1
pip install virtualenv
```

### Create Virtual Environment

```ps1
python -m venv env
```

### Activate _virtual environment_

```ps1
.\env\Scripts\activate
```

### Install required Modules

```ps1
pip install -r requirements.txt
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
