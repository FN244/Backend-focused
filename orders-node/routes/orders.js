const express = require('express');
const router = express.Router();

let orders = []; // This will act as a temporary in-memory store

router.post('/', (req, res) => {
  const { id, item, quantity } = req.body;
  const newOrder = { id, item, quantity };
  orders.push(newOrder);
  res.status(201).json(newOrder);
});

router.put('/:id', (req, res) => {
  const { id } = req.params;
  const { item, quantity } = req.body;
  const orderIndex = orders.findIndex(o => o.id === id);
  
  if (orderIndex > -1) {
    orders[orderIndex] = { id, item, quantity };
    res.json(orders[orderIndex]);
  } else {
    res.status(404).send('Order not found');
  }
});

router.get('/:id', (req, res) => {
  const { id } = req.params;
  const order = orders.find(o => o.id === id);
  
  if (order) {
    res.json(order);
  } else {
    res.status(404).send('Order not found');
  }
});

module.exports = router;
