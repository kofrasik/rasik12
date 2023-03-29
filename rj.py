import streamlit as st
import math

# circle 
def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2*math.pi * radius

def circle_diameter(radius):
    return 2* radius

#rectangle
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2*(length + width)

def rectangle_diagonal(length, width):
    return math.sqrt(length**2 + width**2)

#square
def square_area(side):
   return side**2

def square_perimeter(side):
    return 4*side

def square_diagonal(side):
    return math.sqrt(2)*side

#sphere
def sphere_surfarea(radius):
    return 4 * math.pi * radius ** 2

def sphere_volume(radius):
    return 4/3 * math.pi * radius ** 3

def sphere_radius(sarea):
    return 0.5*math.sqrt(sarea/math.pi)

#cube
def cube_volume(side):
    return side**3

def cube_surfarea(side):
    return 6*side**2

def cube_diagonal(side):
    return math.sqrt(3)*side

# Define the Streamlit app
st.title("2D and 3D Shape Calculator")

# Define the select box for shape type
shape_type = st.selectbox("Select a shape type", ("2D", "3D"))

# Define the select box for specific shape
if shape_type == "2D":
    shape = st.selectbox("Select a 2D shape", ("Circle", "Rectangle","square"))
    if shape == "Circle":
        para_cir = st.selectbox("select your option",("Area of circle","circumference of circle","Diameter of circle"))
    elif shape == "Rectangle":
        para_cir = st.selectbox("select your option",("Area of Rectangle","perimeter of Rectangle","diagonal of Rectangle"))
    elif shape == "square":
        para_cir = st.selectbox("select your option",("Area of square","perimeter of square","diagonal of square"))

else:
    shape = st.selectbox("Select a 3D shape", ("Sphere", "Cube"))
    if shape == "Sphere":
        para_cir = st.selectbox("select your option",("surface area of Sphere","volume of Sphere","radius of Sphere by surface area"))
    elif shape == "Cube":
        para_cir = st.selectbox("select your option",("volume of the cube","surface area of the cube","diagonal of the cube"))


# Define the inputs for the selected shape
if para_cir == "Area of circle":
    radius = st.number_input("Enter the radius of the circle", value=0.0)

elif para_cir == "circumference of circle":
    radius = st.number_input("Enter the radius of the circle", value=0.0)

elif para_cir == "Diameter of circle":
   radius = st.number_input("Enter the radius of the circle", value=0.0)

elif para_cir == "Area of Rectangle":
    length = st.number_input("Enter the length of the rectangle", value=0.0)
    width = st.number_input("Enter the width of the rectangle", value=0.0)

elif para_cir == "perimeter of Rectangle":
    length = st.number_input("Enter the length of the rectangle", value=0.0)
    width = st.number_input("Enter the width of the rectangle", value=0.0)

elif para_cir == "diagonal of Rectangle":
    length = st.number_input("Enter the length of the rectangle", value=0.0)
    width = st.number_input("Enter the width of the rectangle", value=0.0)

elif para_cir == "Area of square":
    side = st.number_input("Enter the side of the square", value=0.0)

elif para_cir == "perimeter of square":
    side = st.number_input("Enter the side of the square", value=0.0)

elif para_cir == "diagonal of square":
    side = st.number_input("Enter the side of the square", value=0.0)

elif para_cir == "surface area of Sphere":
    radius = st.number_input("Enter the radius of the sphere", value=0.0)

elif para_cir == "volume of Sphere":
    radius = st.number_input("Enter the radius of the sphere", value=0.0)

elif para_cir == "radius of Sphere by surface area":
    sarea = st.number_input("Enter the surface area of the sphere", value=0.0)

elif para_cir == "volume of the cube":
    side = st.number_input("Enter the side of the cube", value=0.0)

elif para_cir == "surface area of the cube":
    side = st.number_input("Enter the side of the cube", value=0.0)

elif para_cir == "diagonal of the cube":
    side = st.number_input("Enter the side of the cube", value=0.0)

# Calculate and display the area or volume of the selected shape in a table
if st.button("Calculate"):
    #circle parameters
    if para_cir == "Area of circle":
        area = circle_area(radius)
        st.latex(r"\text{The area of the circle is } \pi r^2 = " + f"{area:.2f}")
        data = {"Shape": [shape], "Radius": [radius], "Area": [area]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "circumference of circle":
        circumference = circle_circumference(radius)
        st.latex(r"\text{circumference of circle } 2\pi r = " + f"{circumference:.2f}")
        data = {"Shape": [shape], "Radius": [radius], "circumference": [circumference]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "Diameter of circle":
        diameter = circle_diameter(radius)
        st.latex(r"\text{diameter of circle } 2 r = " + f"{diameter:.2f}")
        data = {"Shape": [shape], "Radius": [radius], "diameter": [diameter]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "Area of Rectangle":
        Area = rectangle_area(length, width)
        st.latex(r"\text{The area of the rectangle is } lw = " + f"{Area:.2f}")
        data = {"Shape": [shape], "Length": [length], "Width": [width], "Area": [Area]}
        st.write("Data:")
        st.table(data)
    
    elif para_cir == "perimeter of Rectangle":
        perimeter = rectangle_perimeter(length, width)
        st.latex(r"\text{The perimeter of the rectangle is } 2(l+w) = " + f"{perimeter:.2f}")
        data = {"Shape": [shape], "Length": [length], "Width": [width], "perimeter": [perimeter]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "diagonal of Rectangle":
        diagonal = rectangle_diagonal(length, width)
        st.latex(r"\text{The diagonal of the rectangle is } \sqrt(l^2+w^2) = " + f"{diagonal:.2f}")
        data = {"Shape": [shape], "Length": [length], "Width": [width], "diagonal": [diagonal]}
        st.write("Data:")
        st.table(data)
    
    elif para_cir == "Area of square":
        area = square_area(side)
        st.latex(r"\text{Area of square } a^2 = " + f"{area:.2f}")
        data = {"Shape": [shape], "side": [side], "area": [area]}
        st.write("Data:")
        st.table(data)
    
    elif para_cir == "perimeter of square":
        perimeter = square_perimeter(side)
        st.latex(r"\text{perimeter of square } 4.a = " + f"{perimeter:.2f}")
        data = {"Shape": [shape], "side": [side], "perimeter": [perimeter]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "diagonal of square":
        diagonal = square_diagonal(side)
        st.latex(r"\text{diagonal of square } \sqrt2.a = " + f"{diagonal:.2f}")
        data = {"Shape": [shape], "side": [side], "diagonal": [diagonal]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "surface area of Sphere":
        surface_area= sphere_surfarea(radius)
        st.latex(r"\text{surface area of the sphere is } 4\pi r^2 = " + f"{surface_area:.2f}")
        data = {"Shape": [shape], "Radius": [radius], "surface area": [surface_area]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "volume of Sphere":
        volume= sphere_volume(radius)
        st.latex(r"\text{The volume of the sphere is } \frac{4}{3}\pi r^3 = " + f"{volume:.2f}")
        data = {"Shape": [shape], "Radius": [radius], "volume": [volume]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "radius of Sphere by surface area":
        radius =sphere_radius(sarea)
        st.latex(r"\text{The radius of the sphere is } \frac{1}{2}\sqrt\frac{A}{\pi} = " + f"{radius:.2f}")
        data = {"Shape": [shape], "surface area": [sarea], "radius": [radius]}
        st.write("Data:")
        st.table(data)
   
    elif para_cir == "volume of the cube":
        volume = cube_volume(side)
        st.latex(r"\text{The volume of the cube is } a^3 = " + f"{volume:.2f}")
        data = {"Shape": [shape], "side": [side], "volume": [volume]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "surface area of the cube":
        surface_area = cube_surfarea(side)
        st.latex(r"\text{The surface area of the cube is } 6 a^2 = " + f"{surface_area:.2f}")
        data = {"Shape": [shape], "side": [side], "surface_area": [surface_area]}
        st.write("Data:")
        st.table(data)

    elif para_cir == "diagonal of the cube":
        diagonal = cube_diagonal(side)
        st.latex(r"\text{The diagonal of the cube is } \sqrt3.a = " + f"{diagonal:.2f}")
        data = {"Shape": [shape], "side": [side], "diagonal": [diagonal]}
        st.write("Data:")
        st.table(data)
