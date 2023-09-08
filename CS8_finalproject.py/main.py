def make_rails(message, num_rails):
  rails = []
  count = 0
  for i in range(len(message)):
    rails.append(count)
    if (count == 0 or (rails[i-1] < rails[i] and count != num_rails-1)):
      count += 1
    else:
      count -= 1
  return rails

print(make_rails("CHILIBEANSAUCE", 2))
print(make_rails("FRUITSALADGOURD", 4))
