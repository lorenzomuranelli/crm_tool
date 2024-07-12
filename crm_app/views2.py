# crm_app/views.py
import plotly.graph_objects as go
from django.db.models import Sum

class ReportView(APIView):
    def get(self, request):
        # Get sales data
        opportunities = Opportunity.objects.filter(stage='CLOSED_WON')
        data = {
            'labels': [opp.name for opp in opportunities],
            'values': [opp.amount for opp in opportunities],
        }

        # Create a pie chart
        fig = go.Figure(data=[go.Pie(labels=data['labels'], values=data['values'])])
        fig.update_layout(title='Closed Won Opportunities')

        # Render the chart as a JSON response
        chart = fig.to_json()
        return Response({'chart': chart})