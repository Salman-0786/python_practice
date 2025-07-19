def sort_colors(colors, order="asc"):
    if order == "asc":
        return sorted(colors)
    elif order == "desc":
        return sorted(colors, reverse=True)
    else:
        return "Invalid order! Use 'asc' or 'desc'."

colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Violet"]

print("Colors in Ascending Order:")
print(sort_colors(colors, order="asc"))

print("\nColors in Descending Order:")
print(sort_colors(colors, order="desc"))
