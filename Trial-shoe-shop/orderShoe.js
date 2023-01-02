function orderShoes() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('Order Placed Successfully')
    }, 5000);
  });
}

async function asyncCall() {
  console.log("confirming your order...");
  const after = await orderShoes();
  console.log(after)
}

asyncCall();