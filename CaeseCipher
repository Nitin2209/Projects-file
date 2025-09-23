alphabate = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encrypt(original_text, shift_amount):
     cipher_text = " "
     for letter in original_text:
          shifted_position = alphabate.index(letter) + shift_amount

          shifted_position %= len(alphabate) 

          cipher_text += alphabate[shifted_position] 

     print(f"here is the encoded result {cipher_text}")    


def decrypt(original_text, shift_amount):
     output_text = " "
     for letter in original_text:
          shifted_position = alphabate.index(letter) - shift_amount

          shifted_position %= len(alphabate) 

          output_text += alphabate[shifted_position] 

     print(f"here is the decoded result {output_text}")

def caeser (original_text, shift_amount, encode_or_decode):
     output_text = " "
     if encode_or_decode == "decode":
        shift_amount *= -1

     for letter in original_text:

          if letter not in alphabate:
               output_text += letter
          else:     
               

               shifted_position = alphabate.index(letter) + shift_amount

               shifted_position %= len(alphabate) 

               output_text += alphabate[shifted_position] 

     print(f"here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

     direction = input("Typ 'encode' to encrypt, Type 'decode' to decrypt: \n").lower()
     text = input("Type your message: \n").lower()
     shift = int(input ("Type the shift number: \n")) 
     caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)


     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

     if restart == "no":
          should_continue = False
          print("Goodbye")
