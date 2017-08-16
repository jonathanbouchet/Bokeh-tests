#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, ColumnDataSource
from bokeh.models.tools import HoverTool, PanTool, ResetTool, WheelZoomTool

#make a colormap by species
colorMap={'setosa':'red','versicolor':'green','virginica':'blue'}
flowers['color'] = flowers['species'].map(colorMap)

#make a urlmap with links to iris pictures
urlMap={'setosa':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/800px-Kosaciec_szczecinkowaty_Iris_setosa.jpg',
'versicolor':'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/800px-Blue_Flag%2C_Ottawa.jpg',
'virginica':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/800px-Iris_virginica.jpg'}
flowers['imgs'] = flowers['species'].map(urlMap)

#create 3 different glyphs, one per specie
setosa = ColumnDataSource(flowers[flowers["species"]=="setosa"])
versicolor = ColumnDataSource(flowers[flowers["species"]=="versicolor"])
virginica = ColumnDataSource(flowers[flowers["species"]=="virginica"])

#Define the output file path
output_file("iris_custom.html")

TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

#mytooltips = [("Species","@species"),("Sepal width","@sepal_width")]

#custom hover tool
mytooltips ="""
	<div>
		<div>
            <img
            	src="@imgs" height="42" alt="@imgs" width="42"
            	style="float: left; margin: 0px 15px 15px 0px;"
            	border="2"
                ></img>
            </div>
		<div>
			<span style="font-size: 15px; font-weight: bold;">@species</span>
            </div>
            <div>
                <span style="font-size: 10px; color: #696;">Petal length: @petal_length</span><br>
                <span style="font-size: 10px; color: #696;">Petal width: @petal_width</span>
            </div>
        </div>
"""

#Create the figure object
f=figure(tools=TOOLS, toolbar_location='above')

f.select_one(HoverTool).tooltips = mytooltips

#styling plot canvas
f.plot_width = 800
f.plot_height = 600
f.background_fill_color = "#FDE724"
f.background_fill_alpha = 0.25
f.border_fill_color = "black"
f.border_fill_alpha = 0.25

#styling title
f.title.text = "Iris data"
f.title.text_font = "Comic Sans MS"
f.title.text_color = "DarkGreen"
f.title.text_font_size = "30px"

#styling axis
#remove minor tick
f.yaxis.minor_tick_line_color = None
f.xaxis.major_tick_line_color = 'red'
f.yaxis.major_tick_line_color = 'red'
#overwrites previous statement
f.xaxis.minor_tick_in = -6
f.yaxis.major_label_orientation = 'vertical'
#default
f.xaxis.visible = True
f.xaxis.axis_label = "Petal Length"
f.yaxis.axis_label = "Petal Width"

#styling the grid
f.xgrid.grid_line_color = 'black'
f.ygrid.grid_line_color = 'black'

#adding glyphs
f.circle(x="petal_length",y="petal_width",
	size = [i*4 for i in setosa.data["sepal_width"]],
	fill_alpha=.2, color="color",line_dash = [5,3],legend='setosa', source =setosa
	)

f.circle(x="petal_length",y="petal_width",
	size = [i*4 for i in versicolor.data["sepal_width"]],
	fill_alpha=.2, color="color",line_dash = [5,3],legend='setosa', source =versicolor
	)

f.circle(x="petal_length",y="petal_width",
	size = [i*4 for i in virginica.data["sepal_width"]],
	fill_alpha=.2, color="color",line_dash = [5,3],legend='setosa', source =virginica
	)

#Style the legend
#disable legend
f.legend.location = None
#f.legend.location=(575,555)
#f.legend.location='top_left'
#f.legend.background_fill_alpha=0
#f.legend.border_line_color=None
#f.legend.margin=10
#f.legend.padding=18
#f.legend.label_text_color='olive'
#f.legend.label_text_font='times'

#Save and show the figure
show(f)
