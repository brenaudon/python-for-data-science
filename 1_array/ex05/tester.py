from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green
from pimp_image import ft_blue, ft_grey, plot_image


array = ft_load("landscape.jpg")

plot_image(array)

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)
