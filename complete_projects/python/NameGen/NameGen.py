from random import randint, random

beginName = ["Attractive","Bald","Beautiful","Chubby","Clean","Dazzling","Drab","Elegant","Fancy","Fit","Flabby","Glamorous","Gorgeous","Handsome","Long","Magnificent","Muscular","Plain","Plump","Quaint","Scruffy","Shapely","Short","Skinny","Stocky","Ugly","Unkempt","Unsightly"]
endName = ["Actor","Gold","Painting","Advertisement","Grass","Parrot","Afternoon","Pencil","Airport","Guitar","Piano","Ambulance","Hair","Pillow","Animal","Hamburger","Pizza","Answer","Helicopter","Planet","Apple","Helmet","Plastic","Army","Holiday","Honey","Potato","Balloon","Horse","Queen","Banana","Hospital","Quill","Battery","House","Rain","Beach","Hydrogen","Rainbow"]


randName = beginName[randint(0,len(beginName)-1)]+ " " + endName[randint(0,len(endName)-1)]
print(randName)

