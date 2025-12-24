def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price

def main():
    print("Discount Calculator")
    print("Discounts of 20% or higher will be applied")
    
    try:
        # Get original price
        original_price = float(input("Enter the original price: $"))
        
        # Loop until discount is 20% or higher
        while True:
            discount_percent = float(input("Enter the discount percentage: "))
            
            if discount_percent >= 20:
                break
            else:
                print("Discount must be 20% or higher. Please try again.")
        
        # Calculate final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Display result
        print(f"Discount applied: {discount_percent}%")
        print(f"Final price: ${final_price:.2f}")
        print(f"You saved: ${original_price - final_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
