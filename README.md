# LogicScript Language

Example of a basic sr latch:

```txt
;define nor1 NOR 2
;define nor2 NOR 2
;define set_pin PIN IN
;define reset_pin PIN IN
;define out_pin PIN OUT

;attach set_pin nor1
;attach reset_pin nor2
;attach nor1 nor2
;attach nor2 nor1
;attach nor2 out_pin
```
