import qrcode

while True:
  try:
    choose_amount = int(input("How many QR codes do you want to generate (1-10)? "))
  except ValueError:
    print("Please enter a valid number between 1 and 10.")
    continue

  if 1 <= choose_amount <= 10:
    break

  print("Please enter a number between 1 and 10.")

for i in range(choose_amount):
  data = input("Enter the text or URL: ").strip()
  filename = input("Enter the filename: ").strip()

  qr = qrcode.QRCode(box_size=10, border=4)
  qr.add_data(data)

  fill = input("Enter the fill color: ").strip()
  back = input("Enter the background color: ").strip()

  image = qr.make_image(fill_color=fill, back_color=back)
  image.save(filename)
  print(f"QR code saved as {filename}")

print("All QR codes generated successfully!")

#To activate the virtual environment, use the following command in your terminal: source venv/bin/activate
#To deactivate the virtual environment, simply type: deactivate
