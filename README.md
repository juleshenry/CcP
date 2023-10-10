CSS CLI Project (CcP)


```python3 ccp.py --file examples/lines_positive.css --lines 2,3,4,5 --adjustments +1```

```python3 ccp.py --file examples/lines_negative.css --lines 2,3,4,5 --adjustments -1```

```python3 ccp.py --file examples/adjustment_array.css --lines 2,3,4,5 --adjustments 6,-9,4,-20```


Given a file, an array of line numbers, and either an array of adjustments +- px or a singular +- scalar: adjust all lines accordingly.


```ccp --file index.css --regex "example" ```



Given a file, a regex, and either:
    
    an array of adjustments +- px
    
    singular +- scalar: adjust all lines accordingly.
