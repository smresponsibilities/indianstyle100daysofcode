print("Welcome to the tip calculator as tip culture is increasing in India")
a=input("Kitne ka bill hai ₹")
b=input("Tip ki percentage? 10, 12, or 15?")
c=input("Kitne aadmi the")
d=(round((float(a)+(int(b)*float(a))//100)/int(c),2))
#using aadmi as a gender neutral word
print(f"Har ek ko itna cash dena hai ₹{d:.2f}")