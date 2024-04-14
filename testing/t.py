import plotly.graph_objects as go
import plotly.offline as pyo

# Sample data
events = ['Event A', 'Event B', 'Event C']
priorities = [2, 1, 3]
values = [10, 20, 15]

# Sort data by priority
sorted_data = sorted(zip(events, values), key=lambda x: x[1])

# Separate sorted data into events and values
sorted_events, sorted_values = zip(*sorted_data)

# Create the line chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=sorted_events, y=sorted_values, mode='lines+markers'))
fig.update_layout(title='Line Chart', xaxis_title='Event', yaxis_title='Value')

# Save the chart as an HTML file
pyo.plot(fig, filename='line_chart.html')