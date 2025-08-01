const express = require('express');
const orderRoutes = require('./routes/orders');
const app = express();

app.use(express.json());
app.use('/api/orders', orderRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});