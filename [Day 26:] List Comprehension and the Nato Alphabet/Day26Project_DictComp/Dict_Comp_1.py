#Dictionary Comprehension that takex each word in a sentence and calcualtes the number of letters.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

new_dict = {word:len(word) for word in sentence.split()}
print(new_dict)