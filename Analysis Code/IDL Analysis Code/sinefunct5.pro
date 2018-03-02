; Fit a function of the form f(x) = a * sin(x + b) + c to
; sample pairs contained in x and y.
; In this example, a=a(0), b=a(1), c=a(2)
; The partials are easily computed symbolically:
; df/da = sin(x + b)
; df/db = a * cos(x + b)
; df/dc = 1.0
;
pro sineFunct5, x, a, f, pder        ; Function + partials
  ax = sin(x + a(1))
  bx = a(0) * cos(x + a(1))
  f = a(0) * ax + a(2)              ;Evaluate the function
  IF N_PARAMS() ge 4 THEN $         ;Return partials?
     pder= [[ax], [bx], [replicate(1.0, N_ELEMENTS(f))]]
end
