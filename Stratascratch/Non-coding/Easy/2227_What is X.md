# 2227_What is X.md
```yml
Company : Citadel
Difficulty : Easy
Question Type : Technical
Title : What is X
```

- My solution
```
At first, I mistook p for x.
I want to say it’s 4,
but the left side becomes 65 and the right side becomes 64.
I just can’t figure out the prime number that satisfies this equation.
```

- Analyze
```
16p+1=x³
⇒ 16p=x³−1
x³−1=(x−1)(x²+x+1)

Therefore,
16p=(x−1)(x²+x+1)
Since x²+x+1 is always an odd number,
16=24
must all be contained within x−1.

Therefore,
x−1=16k
Substituting this,
p=k(x2+x+1)
Since p is a prime number, the only possible case is k=1.

Therefore,
x−1=16⇒x=17
```
