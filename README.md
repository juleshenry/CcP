CSS CLI Project (CcP)


```python3 ccp.py --file lines_positive.css --lines 3,4,5 --adjustments 5```

```python3 ccp.py --file lines_negative.css --lines 4,5 --adjustments -5```

```python3 ccp.py --file index.css --lines 2,3,4 --adjustments 2,5,-10```


Given a file, an array of line numbers, and either an array of adjustments +- px or a singular +- scalar: adjust all lines accordingly.


```ccp --file index.css --regex "example" ```



Given a file, a regex, and either:
    
    an array of adjustments +- px
    
    singular +- scalar: adjust all lines accordingly.
