name = 'Chris M. Lizama'
age = 27 # not a lie
height = 69 #inches
height_cm = height * 2.54
weight = 200 #pounds
weight_kg = weight * 0.45
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

print "In metric units:", height_cm, "cm tall and", weight_kg, "kg heavy."

#this line is tricky, try to get it right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
