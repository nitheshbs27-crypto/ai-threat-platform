import React, { useEffect, useState } from 'react';
import axios from 'axios';

import { Bar } from 'react-chartjs-2';

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function Analytics() {
  const [labels, setLabels] = useState([]);
  const [values, setValues] = useState([]);

  useEffect(() => {
    loadAnalytics();
  }, []);

  const loadAnalytics = async () => {
    try {
      const res = await axios.get(
        'https://ai-threat-backend-drse.onrender.com/analytics'
      );

      setLabels(res.data.labels);
      setValues(res.data.values);
    } catch (error) {
      console.log(error);
    }
  };

  const data = {
    labels: labels,
    datasets: [
      {
        label: 'Threat Severity Count',
        data: values,
        backgroundColor: '#00ff99',
        borderColor: '#00ff99',
        borderWidth: 1
      }
    ]
  };

  const options = {
    responsive: true,

    plugins: {
      legend: {
        labels: {
          color: 'white'
        }
      }
    },

    scales: {
      x: {
        ticks: {
          color: 'white'
        }
      },

      y: {
        ticks: {
          color: 'white'
        },
        beginAtZero: true
      }
    }
  };

  return (
    <div style={{ padding: '50px' }}>
      <h1>📊 Dynamic Threat Analytics</h1>

      <button
        onClick={loadAnalytics}
        style={{ padding: '10px 20px', marginBottom: '20px' }}
      >
        Refresh Analytics
      </button>

      <div
        style={{
          backgroundColor: '#111827',
          padding: '20px',
          borderRadius: '10px',
          boxShadow: '0px 0px 15px #00ff99'
        }}
      >
        <Bar data={data} options={options} />
      </div>
    </div>
  );
}

export default Analytics;