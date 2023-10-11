CSS CLI Project (CcP)

Given a file, an array of line numbers, and either:
    
    an array of +- scalar adjustments

    OR
    
    a singular +- scalar,
    
adjust all lines accordingly.


```python3 ccp.py --file examples/lines_positive.css --lines 2,3,4,5 --adjustments +1```

```python3 ccp.py --file examples/lines_negative.css --lines 2,3,4,5 --adjustments -1```

```python3 ccp.py --file examples/adjustment_array.css --lines 2,3,4,5 --adjustments 6,-9,4,-20```


Given a file, a regex, and a +- scalar adjustment (--adjustments),

adjust all lines accordingly.


```python3 ccp.py --file examples/index.css --regex "font-size" --adjustments +10```

