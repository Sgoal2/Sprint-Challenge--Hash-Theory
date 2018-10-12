1. * Single regex that matches either of these:

    antelope rocks out
    
    antelopes rock out
A: antelopes? rocks? out?

2. * Regex that matches either of:

    goat
    
    moat

  but not:

    boat
 A:[^b](oat)

 3. regex dates
 A: (\d{1,4})-(\d{1,2})-(\d{1,2})