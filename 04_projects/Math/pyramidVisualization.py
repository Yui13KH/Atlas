import plotly.graph_objects as go

# needs plotly , probably pip install plotly is enough 

# Cube vertices
V = {
    1:(0,0,0), 2:(1,0,0), 3:(1,1,0), 4:(0,1,0),
    5:(0,0,1), 6:(1,0,1), 7:(1,1,1), 8:(0,1,1)
}

pyramids = [
    {"name": "Pyramid 1 (Base: z=0)", "color": "red",   "v": [1, 2, 3, 4, 7]}, 
    {"name": "Pyramid 2 (Base: x=0)", "color": "green", "v": [1, 4, 8, 5, 7]},
    {"name": "Pyramid 3 (Base: y=0)", "color": "blue",  "v": [1, 5, 6, 2, 7]}
]

fig = go.Figure()

for pyr in pyramids:

    pts = [V[i] for i in pyr["v"]]
    x = [p[0] for p in pts]
    y = [p[1] for p in pts]
    z = [p[2] for p in pts]
    
    fig.add_trace(go.Mesh3d(
        x=x, y=y, z=z,
        i=[0, 0, 0, 1, 2, 3],
        j=[1, 2, 1, 2, 3, 0],
        k=[2, 3, 4, 4, 4, 4],
        opacity=0.5,
        color=pyr["color"],
        name=pyr["name"],
        showlegend=True
    ))

edges = [
    (1,2),(2,3),(3,4),(4,1),
    (5,6),(6,7),(7,8),(8,5), 
    (1,5),(2,6),(3,7),(4,8) 
]
for a, b in edges:
    xa, ya, za = V[a]
    xb, yb, zb = V[b]
    fig.add_trace(go.Scatter3d(
        x=[xa, xb], y=[ya, yb], z=[za, zb],
        mode="lines",
        line=dict(color="black", width=2),
        showlegend=False
    ))


fig.update_layout(
    title="Cube Decomposed into 3 Congruent Pyramids (V = 1/3 * B * h)",
    scene=dict(
        aspectmode="cube",
        xaxis=dict(title="X"),
        yaxis=dict(title="Y"),
        zaxis=dict(title="Z")
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

fig.show()