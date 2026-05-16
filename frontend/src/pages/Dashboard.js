import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Dashboard() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    loadAlerts();
  }, []);

  const loadAlerts = async () => {
    try {
      const res = await axios.get(
        'https://ai-threat-backend-drse.onrender.com/alerts'
      );
      setAlerts(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  const totalThreats = alerts.length;
  const criticalThreats = alerts.filter((item) => item.severity === 'Critical').length;
  const highThreats = alerts.filter((item) => item.severity === 'High').length;

  return (
    <div style={{ padding: '50px' }}>
      <h1>⚠ Threat Dashboard</h1>

      <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap' }}>
        <div style={metricCard}>
          <h2>Total Threats</h2>
          <h1>{totalThreats}</h1>
        </div>

        <div style={metricCard}>
          <h2>Critical Threats</h2>
          <h1>{criticalThreats}</h1>
        </div>

        <div style={metricCard}>
          <h2>High Threats</h2>
          <h1>{highThreats}</h1>
        </div>
      </div>

      <br />

      <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap' }}>
        {alerts.map((item, index) => (
          <div key={index} style={alertCard}>
            <h2 style={{ color: '#00ff99' }}>🚨 Threat Alert</h2>
            <p><b>IP:</b> {item.ip}</p>
            <p><b>Threat:</b> {item.threat_type}</p>
            <p><b>Severity:</b> {item.severity}</p>
            <p><b>Score:</b> {item.score}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

const metricCard = {
  backgroundColor: '#111827',
  border: '1px solid #00ff99',
  borderRadius: '12px',
  padding: '25px',
  width: '250px',
  boxShadow: '0px 0px 15px #00ff99',
  textAlign: 'center',
};

const alertCard = {
  backgroundColor: '#111827',
  border: '1px solid #00ff99',
  borderRadius: '10px',
  padding: '20px',
  width: '300px',
  boxShadow: '0px 0px 15px #00ff99',
};

export default Dashboard;