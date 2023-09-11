from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings
from django.urls import resolve
from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme
from pprint import pprint

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""

from django.shortcuts import render
import os
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import matplotlib.font_manager as fm
import geopandas as gpd
import pandas as pd

from django.views.generic import TemplateView
import matplotlib
matplotlib.use('Agg')  # Choose an appropriate backend, 'Agg' for non-interactive use
import matplotlib.pyplot as plt

import os
import geopandas as gpd
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.views import View

class InteractiveMapView(View):
    template_name = 'pages/threews/dynamic-map.html'


    def get(self, request, *args, **kwargs):

        # Add your additional context data here if needed
        
        # Step 1: Read all CSV files from the data folder
        data_folder = os.path.join('assets', 'data_3Ws')
        csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]

        # Step 2: Concatenate all dataframes
        dataframes = []
        for file in csv_files:
            df = pd.read_csv(os.path.join(data_folder, file))
            dataframes.append(df)
        all_data = pd.concat(dataframes, ignore_index=True)

        # Read in the admin2 shapefile
        shp2 = gpd.read_file(os.path.join('assets', 'data/nga_adm_osgof_20190417/nga_admbnda_adm2_osgof_20190417.shp'))
        shp2 = shp2[['ADM2_EN', 'geometry']]

        # Count unique organizations in each LGA for each year
        data_unique_org = all_data.drop_duplicates(subset=['lga', 'organisation', 'year'])
        org_count = data_unique_org.groupby(['lga', 'year']).size().reset_index(name='unique_org_count')

        # Convert 'year' back to integer
        org_count['year'] = org_count['year'].astype(int)

        # Count total activities in each LGA for each year
        activity_count = all_data.groupby(['lga', 'year']).size().reset_index(name='activity_count')
        activity_count['year'] = activity_count['year'].astype(int)  # Convert 'year' back to integer

        # Count unique project sectors in each LGA for each year
        data_unique_sector = all_data.drop_duplicates(subset=['lga', 'project_sector', 'year'])
        sector_count = data_unique_sector.groupby(['lga', 'year']).size().reset_index(name='unique_project_sector_count')
        sector_count['year'] = sector_count['year'].astype(int)  # Convert 'year' back to integer

        # Merge the counts with the shapefile
        merge = shp2.merge(org_count, left_on='ADM2_EN', right_on='lga', how='left')
        merge = merge.merge(activity_count, on=['lga', 'year'], how='left')
        merge = merge.merge(sector_count, on=['lga', 'year'], how='left')

        # Create an interactive map using Plotly Express with animation based on year
        fig = px.choropleth(merge,
                            geojson=merge['geometry'],
                            locations=merge.index,
                            color='unique_org_count',
                            hover_name='ADM2_EN',
                            hover_data=['unique_org_count', 'activity_count', 'unique_project_sector_count'],
                            animation_frame='year',
                            title='Organisations by LGA',
                            labels={'unique_org_count': 'Unique Organisations', 'activity_count': 'Total Activities', 'unique_project_sector_count': 'Project Sectors'},
                            color_continuous_scale='OrRd')

        # Set the map boundaries to focus on Adamawa, Borno, and Yobe
        fig.update_geos(fitbounds="locations", visible=False, center={"lat": 11.5, "lon": 13}, projection_scale=7)

        # Adjust the size of the map frame and hide the color scale
        fig.update_layout(
            autosize=True,  # Automatically adjust the map size
            margin=dict(l=0, r=0, t=0, b=0),  # Remove margins
            coloraxis_showscale=False
        )
        fig.update_traces(marker_line=dict(color='Gray', width=0.1))

        # Render the map in the template
        context = {'map_div': fig.to_html()}
        context = KTLayout.init(context)

    
        # Add your additional context data here if needed
        return render(request, self.template_name, context)


        
        

'''
class InteractiveMapView(TemplateView):
    template_name = 'pages/threews/dynamic-map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add your additional context data here if needed
        context = KTLayout.init(context)

        
        
        return context
'''

class MapView(TemplateView):
    template_name = 'pages/threews/index.html'

    def generate_map(self, columns):
        map_paths = []  # Initialize map_paths list

        shpfile1 = os.path.join('assets', 'data/nga_adm_osgof_20190417/nga_admbnda_adm1_osgof_20190417.shp')
        shpfile2 = os.path.join('assets', 'data/nga_adm_osgof_20190417/nga_admbnda_adm2_osgof_20190417.shp')
        csvfile = os.path.join('assets', 'data/data_Graphs/3Ws_Maps.csv')

        # Read in the admin2 shapefile
        shp2 = gpd.read_file(shpfile2)
        shp2 = shp2[['ADM2_EN', 'geometry']]

        # Read in the admin1 shapefile
        shp1 = gpd.read_file(shpfile1)

        # Filter the admin1 shapefile to only include the states of Adamawa, Borno and Yobe
        shp1 = shp1[shp1['ADM1_EN'].isin(['Adamawa', 'Borno', 'Yobe'])]

        # Import csv data
        data = pd.read_csv(csvfile)
        data = data.groupby('LGA').sum()

        merge = shp2.join(data, on='ADM2_EN')
        # join the shapefile with the dataframe
        
        # Create a folder called "AI_Maps" if it doesn't exist
        folder_name = os.path.join('assets', 'ai_maps')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Set common plot settings
        plot_settings = {
            'edgecolor': 'Gray',
            'linewidth': 0.1,
            'linestyle': (0, (5, 10)),  # Set the linestyle to a custom pattern (5 units of line, 10 units of space)
            'legend': False,  # Disable automatic legend
            'figsize': (10, 5)
        }

        # Set the font properties for the legend numbers
        font_path = os.path.join('assets', 'data/RobotoCondensed-Regular.ttf')  # Provide the actual path to the Roboto Condensed Regular font file
        font_prop = fm.FontProperties(fname=font_path, size=10)

        for col in columns:
            fig, ax = plt.subplots()

            cmap = plt.get_cmap('OrRd')
            cmap.set_under('white')

            merge.plot(column=col, cmap=cmap, vmin=0.01, **plot_settings, ax=ax)
            plt.title(col)

            # Overlay the admin1 shapefile with no fill and gray lines
            shp1.plot(ax=ax, facecolor='none', edgecolor='Gray', linewidth=0.3)

            # Get the minimum and maximum values of the column
            vmin = merge[col].min()
            vmax = merge[col].max()

            if vmin < 1:
                # If there are negative values, adjust the colorbar limits
                bounds = np.linspace(1, vmax, 6)
                norm = colors.BoundaryNorm(bounds, cmap.N)
                sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
                sm.set_array([])  # Dummy array for the colorbar

                # Add the colorbar on the left side
                cbar = plt.colorbar(sm, ax=ax, label='Legend', extend='min', orientation='vertical', pad=0.05)
                cbar.ax.set_yticklabels([f'{int(np.ceil(val)):.0f}' for val in bounds])  # Round up the numbers to whole integers

                # Reduce the height of the colorbar
                cbar.ax.set_position([cbar.ax.get_position().x0, cbar.ax.get_position().y0, 
                                    cbar.ax.get_position().width, cbar.ax.get_position().height * 0.4])

                # Set the font properties for the legend numbers
                cbar.ax.tick_params(axis='y', labelsize=10)
                for label in cbar.ax.yaxis.get_ticklabels():
                    label.set_font_properties(font_prop)

            # Remove scale and frame around the map
            ax.set_axis_off()

            # Export the plot as a PNG image
            image_path = os.path.join(folder_name, f'map_{col}.svg')
            plt.savefig(image_path, format='svg', bbox_inches='tight', pad_inches=0)
            plt.close()  # Close the figure

            map_paths.append(image_path)

        return map_paths

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add your additional context data here if needed
        context = KTLayout.init(context)

        # Include vendors and javascript files for dashboard widgets

        # Generate maps and add their paths to the context
        columns = ['Overall']
        map_paths = self.generate_map(columns)

        context['map_paths'] = map_paths

        return context


