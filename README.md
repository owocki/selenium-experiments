# [ecommerce site name] Store Tester

This repo has python script(s) that verify functionality on the [ecommerce site name]

# Why

To automatically verify that [ecommerce site name] is worrking

# Roadmap

Roadmap will be flushed out based upon priority of the verificadtion.  Question to ask before prioritizng something: Will this prioritization affect CPA of our store?

# Supported Functionality
* [X] User can check out

# Future Functionality
* [ ] Alerting
* [ ] Performance Checks -- What if the selenium tests timeout?
* [ ] User can view order status

# To install & run

1. Download `ChromeDriver` [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Place it at `/Applications/chromedriver` on your local filesystem.
2. Run thar commands:

```bash
cd /path/to/repo
pip install -r requirements.txt
python test_that_stores_working.py
```
3. Optional: Flip to `production_mode` by toggling these variables

```python
SETTINGS = TEST_SETTINGS
```

```python
SETTINGS = PRODUCTION_SETTINGS
```


