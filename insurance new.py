print("Vehicle Details")
make = input("Car Make: " )
model = input("Model: " )
year = input("Year Purchased: " )
driver_name = input("Name Of The Driver: " )
driver_age = input("Driver Age: " )
car_value = int(input("Value Of The Car: " ))
accessory = int(input("Value Of The Accessories: " ))
experience = int(input("Experience Of The Driver"))

if make == "maruti":
    make_value = 500
if model == "swift":
    model_value = 50
if model == "xl6":
    model_value = 60
if model == "ertiga":
    model_value = 70
    
if make == "hyuandai":
    make_value = 600
if model == "i10":
    model_value = 25
if model == "i20":
    model_value = 50
if model == "creta":
    model_value = 75    

if make == "kia":
    make_value = 700   
if model == "seltose":
    model_value = 40
if model == "sonet":
    model_value = 55
if model == "carnival":
    model_value = 80


if car_value >= 0 and car_value<=  100000:
    car_premium = 800
if car_value >= 100001 and car_value<=  500000:
    car_premium = 1000
if car_value >= 500001 and car_value<=  1000000:
    car_premium = 1200
if car_value >= 1000000:
    car_premium = 1400

    
accessory_value = accessory*0.1

total = car_premium + accessory_value + make_value + model_value

experience_value = experience/100*total

print(f"""            JEFFREY's INSURANCE COMPANY

          premium for car value  =  ${car_premium}
          premium for accessory value  =  +${accessory_value}
          premium for make  =  +${make_value}
          premium for model  =  +${model_value}
          discoumt for experience = -${experience_value}
          [{experience}% on {total}]
          the total premium to be paid = ${total - experience_value}
          """)
          


