import folium
import geopandas as gpd
from shapely.geometry import MultiLineString
from shapely.geometry import LineString
import pandas as pd
from folium.plugins import HeatMap
from folium.plugins import TimestampedGeoJson
from dotenv import load_dotenv
import os
load_dotenv()

gdf = gpd.read_file('export.geojson')
gdf_extra = gpd.read_file('mauritania_1.kml')
m = folium.Map(
    location=[29.56, -7.10],
    zoom_start=6,
    tiles="OpenStreetMap",
    max_bounds=True,
    min_lat=19.0,
    max_lat=38.0,
    min_lon=-18.0,
    max_lon=2.0,
)

un_group = folium.FeatureGroup(name='UN/ MINURSO')
sadr_group = folium.FeatureGroup(name='SADR/POLISARIO')
berm_zones = folium.FeatureGroup(name='Berm and zones')
petrolium_line = folium.FeatureGroup(name='Gas pipelines')


folium.Marker(
    location=[21.426, -16.959],
    popup=folium.Popup('''🚚 In <b>autumn 2020</b>, <br>
  <b>POLISARIO</b> supporters blocked the road, <br>
  preventing lorries from travelling <br>
  between <b>Morocco</b> and <b>Mauritania</b>. <br>
  <br>
  💥 On <b>13 November 2020</b>, <br>
  <b>Moroccan forces</b> began operations <br>
  to disperse the protests; <br>
  the <b>POLISARIO</b> Front regarded <br>
  these actions as an act of aggression <br>
  and revoked the ceasefire. ''', max_width=300), tooltip='El-Ghergerat').add_to(m)

folium.Marker(
    location=[27.15, -13.20],
    popup=
        folium.Popup('''🏢The largest city in the territory <br> 
                      <b>claimed</b> by Western Sahara (POLISARIO). <br>
                      <b>De jure</b>, it is the capital of Western Sahara. <br>  
                      <b>De facto</b>, it is controlled by Morocco.''', max_width=300), tooltip='Laayoune').add_to(m)

folium.Marker(
    location=[26.128026898495893, -10.538949646087243],
    popup=
        folium.Popup('''🌐The current field camp for <b>military observers
        <b>(MINURSO)</b> and airfield''', max_width=300), tooltip='Tifariti-MINURSO', icon=folium.Icon(color='lightblue', icon='binoculars', prefix='fa')).add_to(un_group)

folium.Marker(
    location=[26.16068854738046, -10.563440227039939],
    popup=
        folium.Popup('''⭐The de facto capital of the Sahrawi Arab Democratic Republic''', max_width=300), tooltip='Tifariti-SADR', icon=folium.Icon(color='darkgreen', icon='star', prefix='fa')).add_to(sadr_group)

folium.Marker(
    location=[27.473071930359648, -8.08775032878478],
    popup=
        folium.Popup('''🪖The headquarters of the POLISARIO and the SADR''', max_width=300), tooltip='Rabouni-SADR', icon=folium.Icon(color='darkgreen', icon='gun', prefix='fa')).add_to(sadr_group)

folium.Marker(
    location=[27.67528, -8.12861],
    popup=
        folium.Popup('''🌐The <b>MINURSO Liaison Office</b> in Tindouf.
        It maintains contact with the POLISARIO headquarters and the Algerian government. 
        In addition, it serves as the security coordinator for UN 
        agencies working with refugees in the camps. ''', max_width=300), tooltip='Tindouf-Liaison Office', icon=folium.Icon(color='darkblue', icon='rss', prefix='fa')).add_to(un_group)

folium.Marker(
    location=[27.154334561622118, -13.191487771529394],
    popup= folium.Popup(
        '''🌐The city of Laayoune is home to the main facilities of the UN mission MINURSO. 
        Specifically, these include the mission headquarters and a medical unit staffed by 
        foreign personnel. In addition, the city also houses the operation’s main logistics center.''',
        max_width=300),
    tooltip='Laayone-MINURSO', icon=folium.Icon(color='darkblue', icon='building', prefix='fa')).add_to(un_group)


folium.Marker(
    location=[26.73944, -11.67028],
    popup= folium.Popup(
        '''🌐MINURSO Military Observer Field Base (Team Site Smara) - Operational Logistics Center and Helicopter Base''',
        max_width=300),
    tooltip='Smara-MINURSO', icon=folium.Icon(color='lightblue', icon='binoculars', prefix='fa')).add_to(un_group)

folium.Marker(
    location=[27.416, -9.051],
    popup= folium.Popup(
        '''🌐MINURSO Military Observer Field Base (Mahbas Team Site) ''',
        max_width=300),
    tooltip='Mahbas-MINURSO', icon=folium.Icon(color='lightblue', icon='binoculars', prefix='fa')).add_to(un_group)

folium.Marker(
    location=[24.1015, -13.2757],
    popup= folium.Popup(
        '''🌐 MINURSO Military Observer Field Base (Um Dreiga Team Site) ''',
        max_width=300),
    tooltip='Um Dreiga-MINURSO', icon=folium.Icon(color='lightblue', icon='binoculars', prefix='fa')).add_to(un_group)

folium.Marker(
    location=[22.53639, -14.28583],
    popup= folium.Popup(
        '''🌐MINURSO Military Observer Field Base (Team Site Awsard) - Operational Logistics Center and Helicopter Base''',
        max_width=300),
    tooltip=' Awsard-MINURSO', icon=folium.Icon(color='lightblue', icon='binoculars', prefix='fa')).add_to(un_group)

folium.Marker(
    location=[	26.34944, -9.57556],
    popup= folium.Popup(
        '''🌐MINURSO Military Observer Field Base (Team Site Bir Lahlou) - The capital of the SADR from 1976 to 2008''',
        max_width=300),
    tooltip=' Bir Lahlou-MINURSO', icon=folium.Icon(color='lightblue', icon='binoculars', prefix='fa')).add_to(un_group)

folium.Marker(
    location=[26.14722, -11.06917],
    popup= folium.Popup(
        '''🌐MINURSO Military Observer Field Base (Team Site Mehaires) - A drone strike occurred not far from the UN post''',
        max_width=300),
    tooltip='Mehaires-MINURSO', icon=folium.Icon(color='lightblue', icon='binoculars', prefix='fa')).add_to(un_group)

folium.Marker(
    location=[23.48, -12.84],
    popup= folium.Popup(
        '''🌐MINURSO Military Observer Field Base (Team Site Mijek)''',
        max_width=300),
    tooltip='Mijek-MINURSO', icon=folium.Icon(color='lightblue', icon='binoculars', prefix='fa')).add_to(un_group)

folium.Marker(
    location=[22.18333, -13.13306	],
    popup= folium.Popup(
        '''🌐MINURSO Military Observer Field Base (Team Site Agwanit)''',
        max_width=300),
    tooltip='Agwanit-MINURSO', icon=folium.Icon(color='lightblue', icon='binoculars', prefix='fa')).add_to(un_group)

folium.Circle(location=[27.6179, -7.9216], radius=16800, popup=folium.Popup('''🏠Refugee camps for Western Saharans. The administrative section of the SADR, managed by the POLISARIO Front. UN observers are present in the camps.''', max_width=300), color='green', fill=True, fill_opacity=0.2, tooltip='🏠Refugee Camps').add_to(sadr_group)

for index, row in gdf.iterrows():
    geom = row.geometry
    points = [[lat, lon] for lon, lat in geom.coords]
    folium.PolyLine(locations=points, color='red', tooltip='🧱The Moroccan Wall Against the POLISARIO (Wall of Shame)').add_to(berm_zones)

for filename in ['mauritania_1.kml', 'mauritania_2.kml']:
    gdf_extra = gpd.read_file(filename)
    for index, row in gdf_extra.iterrows():
        geom = row.geometry
        coords = [[lat, lon] for lon, lat, alt in geom.coords]
        folium.PolyLine(locations=coords, color='red', tooltip='🧱The Moroccan Wall Against the POLISARIO (Wall of Shame)').add_to(berm_zones)

folium.PolyLine(
    locations=[[32.94675255220963, 3.237991832366821], [33.76320920867968, 2.815068450547082], [35.36970401065378, 1.3172901057684192], [35.28290002346393, -1.4186413535960285], [36.8431912262068, -2.348656168976354]],
    color='orange',
    weight=5,
    popup=folium.Popup('''🟢Medgaz Gas Pipeline. <br>
        Capacity expanded by <b>34%</b> (8 → 10.7 bcm/year) in late 2021, <br>
        via a fourth compressor at Beni Saf timed to absorb the volume <br>
        lost from the Maghreb-Europe closure.''', max_width=300),
    tooltip='Medgaz Gas Pipeline'
).add_to(petrolium_line)

folium.PolyLine(
    locations=[[32.94675255220963, 3.237991832366821], [32.61681822625435, 0.20493911228142023], [33.88124945050985, -1.6108277172786185], [34.62902794820483, -4.713687521308473], [35.6397768293625, -5.493716782161179], [36.27561188779152, -5.5761142392935055], [37.87545475359869, -4.8116574453971275]],
    color='blue',
    weight=5,
    dash_array = '10, 6',
    popup=folium.Popup('''🔴Maghreb-Europe Gas Pipeline. <br>
    Closed on <b>31 October 2021</b>, synchronized with the diplomatic <br>
    rupture between Algeria and Morocco. In 2022, part of the line <br>
    was reversed to supply Morocco from Spain instead.''', max_width=300),
    tooltip='Maghreb-Europe Gas Pipeline',
).add_to(petrolium_line)

folium.PolyLine(
    locations=[[32.94675255220963, 3.237991832366821], [35.827043670349504, 8.249138232698611], [37.051079004390516, 11.010856343997592], [37.66815958603765, 12.54071123301983], [37.70051820128492, 14.692954702972433], [38.96905652500352, 16.515998814478884], [39.83397077650748, 16.425463922299656], [40.80660087727603, 15.14562933984923]],
    color='violet',
    weight=5,
    popup=folium.Popup('''🟢 Trans-Mediterranean (Transmed) Pipeline. <br>
    In April 2022, Eni and Sonatrach agreed to gradually raise <br>
    throughput by up to <b>9 bcm/year by 2023-24</b>, as Italy sought <br>
    to reduce reliance on Russian gas after the invasion of Ukraine.''', max_width=300),
    tooltip='Trans-Mediterranean (Transmed) Pipeline'
).add_to(petrolium_line)




gdf_extra1 = gpd.read_file('mauritania_1.kml')
gdf_extra2 = gpd.read_file('mauritania_2.kml')
total_gdf = list(gdf.geometry) + list(gdf_extra1.geometry) + list(gdf_extra2.geometry)
tot_geo = gpd.GeoSeries(total_gdf, crs='EPSG:4326')
tot_geo = tot_geo.to_crs(epsg=32628)
merged = tot_geo.union_all()
restricted_area = merged.buffer(30000)
buffer_strip = merged.buffer(5000)
restricted_area_geo = gpd.GeoSeries([restricted_area], crs=32628).to_crs(epsg=4326)
buffer_strip_geo = gpd.GeoSeries([buffer_strip], crs=32628).to_crs(epsg=4326)
folium.GeoJson(restricted_area_geo, style_function=lambda x: {'color': 'purple', 'fillOpacity': 0.1, 'stroke': False}, tooltip='Restricted Area (30 km)').add_to(berm_zones)
folium.GeoJson(buffer_strip_geo, style_function=lambda x: {'color': 'red', 'fillOpacity': 0.3, 'stroke':False}, tooltip='Buffer Strip (5 km)').add_to(berm_zones)

ucdp_list = pd.read_csv('ucdp_clean.csv')
#change coords a little bit for better explore map information
ucdp_list.loc[ucdp_list["id"] == 391501.0, "latitude"] = 21.333512788067424
ucdp_list.loc[ucdp_list["id"] == 391501.0, "longitude"] =  -16.947018417227095

ucdp_list.loc[ucdp_list["id"] == 396479.0, "latitude"] = 26.145
ucdp_list.loc[ucdp_list["id"] == 396479.0, "longitude"] = -10.580

ucdp_list.loc[ucdp_list["id"] == 428221.0, "latitude"] = 26.020
ucdp_list.loc[ucdp_list["id"] == 428221.0, "longitude"] = -12.110

ucdp_list.loc[ucdp_list["id"] == 436462.0, "latitude"] = 26.006
ucdp_list.loc[ucdp_list["id"] == 436462.0, "longitude"] = -12.083

ucdp_for_map = []

def make_popup(emoji, title, date, body, best, high, side, source_name, source_url):
    return f'''
    <div style="font-family: Arial, sans-serif; max-width: 280px;">
        <div style="font-size:15px; font-weight:bold; margin-bottom:4px;">{emoji} {title}</div>
        <span style="background:#eee; color:#555; font-size:11px; padding:2px 8px; border-radius:10px;">{date}</span>
        <div style="font-size:13px; line-height:1.4; margin-top:8px; margin-bottom:8px;">{body}</div>
        <div style="font-size:12px; margin-bottom:6px;"><div style="font-size:12px; margin-bottom:6px;">
    📊 Best: <b>{best}</b> ({side}) <br>
    📈 High: <b>{high}</b> ({side})
</div>
        <hr style="margin:6px 0; border:none; border-top:1px solid #eee;">
        <div style="font-size:11px; color:#888;">SOURCE: <a href="{source_url}" target="_blank" style="color:#888;">{source_name}</a></div>
    </div>
    '''
ucdp_texts = {
    391501: make_popup(
        "🚚",
        "Clashes in Guerguerat",
        "14.11.2020",
        "The incident began when Moroccan forces entered Guerguerat to disperse protesters and break the road blockade (November 13). According to a source citing POLISARIO and the Western Sahara army, shelling occurred a day or two later, allegedly killing 2 Moroccan soldiers.",
        2, 2, "Morocco",
        "Atalayar",
        "https://atalayar.com/en/articulo/politics/polisario-front-claims-have-caused-deaths-against-moroccan-army/20201115103713148419.html"
    ),
    385664: make_popup(
        "💥",
        "Shelling of Moroccan Army Garrison near Ouarkziz",
        "08.02.2021",
        "POLISARIO carried out an attack on a Moroccan armed forces garrison. According to POLISARIO's statements, 3 Moroccan soldiers were killed; Morocco's Prime Minister publicly called this a 'media war.'",
        0, 3, "Morocco (disputed)",
        "",
        ""
    ),
    385685: make_popup(
        "💥",
        "Shelling of Moroccan Forces near Touizgui (the Berm)",
        "21.02.2021",
        "The Ministry of Defense of the Sahrawi Arab Democratic Republic (POLISARIO Front) announced large-scale attacks on Moroccan forces. The attacks consisted of massed shelling of Moroccan forces near the sand wall (the 'Wall of Shame'). In response, Morocco subsequently began actively using drones.",
        0, 5, "Morocco (unconfirmed)",
        "North Africa Post",
        "https://north-africa.com/western-sahara-tensions-running-high-as-polisario-front-says-three-moroccan-soldiers-killed-in-attack-in-touizgui/"
    ),
    396479: make_popup(
        "✈️",
        "Drone Strike Kills Head of POLISARIO Gendarmerie",
        "06.04.2021",
        "The head of the POLISARIO gendarmerie was killed by a drone strike on April 6, 2021. This is considered one of the first documented uses of drones by Morocco in this conflict.",
        3, 3, "POLISARIO",
        "AFP / Jeune Afrique; UN Secretary-General report S/2021/843",
        ""
    ),
    420096: make_popup(
        "🚚",
        "Shelling of Algerian Drivers",
        "01.11.2021",
        "According to Algeria, a Moroccan strike in the border area between Mauritania and Western Sahara killed 3 civilian drivers.",
        3, 3, "Civilians",
        "Reuters",
        "https://www.reuters.com/world/algeria-says-moroccan-bombardment-killed-three-algerians-western-sahara-border-2021-11-03/"
    ),
    423699: make_popup(
        "💀",
        "Mijek: Accusation of Civilian Shelling",
        "14.11.2021",
        "In mid-November, the POLISARIO Front accused Moroccan armed forces of killing 11 civilians in drone strikes on November 14-15 in the Mijek area of Western Sahara, an area controlled by POLISARIO. The event may be linked to the upcoming UN vote on the mission's mandate in the region.",
        0, 11, "Civilians (alleged)",
        "CrisisGroup - CrisisWatch (November 2021)",
        ""
    ),
    428221: make_popup(
        "💀",
        "Mauritanian Gold Prospectors",
        "03.01.2022",
        "CrisisWatch (January 2022) reported that a Moroccan drone strike on January 3 killed three Mauritanian civilians in the UN buffer zone. Such incidents have occurred before, though identifying casualties is sometimes difficult given where these events take place.",
        3, 3, "Civilians",
        "CrisisGroup - CrisisWatch (January 2022)",
        ""
    ),
    428222: make_popup(
        "✈️",
        "Drone Strike on the Mehaires Area",
        "10.01.2022",
        "Sources close to the Saharawi peace movement reported in mid-January that a drone strike killed four POLISARIO members in the eastern Mehaires area of Western Sahara, controlled by POLISARIO.",
        4, 4, "POLISARIO",
        "CrisisGroup - CrisisWatch (January 2022)",
        ""
    ),
    436462: make_popup(
        "🚚",
        "Airstrike on a Truck",
        "10.04.2022",
        "Media affiliated with the POLISARIO independence movement reported that a Moroccan airstrike hit trucks near the border between the disputed territory and Mauritania early Sunday morning, killing three people of unknown nationality. Because Algeria made a similar accusation to the one on January 3, 2022, this may refer to the same incident.",
        3, 3, "Unidentified",
        "The New Arab",
        "https://www.newarab.com/news/algeria-accuses-morocco-killing-3-edge-w-sahara"
    ),
    464209: make_popup(
        "💥",
        "Clashes Along the Berm",
        "15.11.2022",
        "According to MINURSO reports, Moroccan forces used aircraft and artillery to repeatedly strike POLISARIO forces attempting to cross the wall at various points.",
        4, 4, "POLISARIO",
        "UN reports (indirect)",
        ""
    ),
    511311: make_popup(
        "💀",
        "Explosions in Smara",
        "29.10.2023",
        "On October 29, four explosions occurred in the city of Smara in Morocco's southern provinces, killing one young man and wounding three others, two of them critically. The blast struck three residential neighborhoods and was not directed at any military bases or positions in the area. The POLISARIO Front claimed responsibility through its press office; its representative to the European Union later justified the attack, stating that Morocco also strikes Saharawi civilians with drones.",
        1, 1, "Unidentified",
        "Washington Institute",
        "https://www.washingtoninstitute.org/policy-analysis/polisario-attack-smara-worrying-escalation-morocco"
    ),
    565367: make_popup(
        "💥",
        "Strike on POLISARIO in Al-Hauza",
        "18.01.2025",
        "Moroccan media reported a strike on the POLISARIO Front, as reflected in the CrisisWatch report for January 2025.",
        3, 3, "POLISARIO",
        "CrisisGroup - CrisisWatch (January 2025)",
        ""
    ),
}
for i, row in ucdp_list.iterrows():
    if pd.isna(row["longitude"]) or pd.isna(row["latitude"]) or pd.isna(row["date_start"]):
        continue

    if row["best"] == 0:
        color = "gray"
    elif row["deaths_a"] > 0:
        color = "red"
    elif row["deaths_b"] > 0:
        color = "darkgreen"
    elif row["deaths_civilians"] > 0:
        color = "black"
    else:
        color = "orange"
    text = ucdp_texts.get(int(row["id"]), "")

    ucdp_for_map.append({
        "coords": [float(row["longitude"]), float(row["latitude"])],
        "date": str(row["date_start"]),
        "color": color,
        "text": text
        })

features = []
for event in ucdp_for_map:
    features.append({
        "type": "Feature",
        "geometry": {
            "type": "MultiPoint",
            "coordinates": [event["coords"]]
        },
        "properties": {
            "times": [event["date"]],
            "popup": event["text"],
            "icon": "circle",
            "iconstyle": {
                "fillColor": event["color"],
                "color": event["color"],
                "fillOpacity": 0.8,
                "radius": 6
            }
        }
    })

TimestampedGeoJson(
    {"type": "FeatureCollection", "features": features},
    period="P1M",
    duration=None,
    transition_time=500,
    auto_play=False
).add_to(m)
un_group.add_to(m)
sadr_group.add_to(m)
petrolium_line.add_to(m)
berm_zones.add_to(m)
folium.LayerControl(collapsed=False).add_to(m)
legend_html = '''
<div style="position: fixed; bottom: 30px; left: 30px; z-index: 1000;
     background: white; padding: 12px 14px; border-radius: 8px;
     box-shadow: 0 2px 6px rgba(0,0,0,0.3); font-family: Arial, sans-serif; font-size: 12px; max-width: 230px;">
    <b style="font-size:13px;">Legend</b><br><br>

    <b>UN / MINURSO</b><br>
    <span style="color:#ADD8E6;">●</span> Team site<br>
    <span style="color:#00008B;">●</span> HQ / Liaison office<br><br>

    <b>POLISARIO / SADR</b><br>
    <span style="color:darkgreen;">●</span> Capital / HQ<br>
    <span style="color:green;">■</span> Refugee camps<br><br>

    <b>Berm & zones</b><br>
    <span style="color:red;">▬</span> Berm (wall)<br>
    <span style="color:purple;">■</span> Restricted Area (30 km)<br>
    <span style="color:red;">■</span> Buffer Strip (5 km)<br><br>

    <b>Gas pipelines</b><br>
    <span style="color:orange;">▬</span> Medgaz (active)<br>
    <span style="color:blue;">▬</span> Maghreb-Europe (closed, dashed)<br>
    <span style="color:violet;">▬</span> Transmed<br><br>

    <b>UCDP incidents (by side)</b><br>
    <span style="color:red;">●</span> Morocco<br>
    <span style="color:darkgreen;">●</span> POLISARIO<br>
    <span style="color:black;">●</span> Civilians<br>
    <span style="color:orange;">●</span> Unidentified<br>
    <span style="color:gray;">●</span> Disputed / unconfirmed
</div>
'''
gray_css = '<style>.leaflet-tile-pane { filter: grayscale(90%); }</style>'
m.get_root().html.add_child(folium.Element(gray_css))
m.get_root().html.add_child(folium.Element(legend_html))
m.save('map.html')