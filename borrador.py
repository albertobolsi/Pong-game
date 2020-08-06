play_again = "nope"
affirmative = ["Yes","yes","Y","Yep","yep"]
negative = ["No","no","N","Nope","nope"]
aff_answer = any(element in play_again for element in affirmative)
neg_answer = any(element in play_again for element in negative)

print(aff_answer)
print(neg_answer)
