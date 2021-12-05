
# Production

### Rendering product size:
* Dictionary renders [{ Product Name: Size }] in the size field on the shopping bag page instead of just the size chosen.
### FIX: 
* Appended key/value pair for quantity in bag items context processor else statement - with thanks to scott from Tutor Support @ [Code Institute](https://codeinstitute.net/) for pointing out the typo.
### Quantity input:
* Quantity input box not working when I click on the chevron buttons to increase or decrease product quantity in the shopping bag.
### FIX: 
* Syntax error: When I copied and pasted input box code from my product detail page I didn't include the closing div tag and didn't update value field to {{ item.item_quantity }}.
### Delete Product:
* Delete function not working, print statement in except Exception returns "POST /shopping_bag/delete/26/ HTTP/1.1" 500 0 'extra small'
### FIX: 
* Fixed typo in delete function in views removed [size] from line 63, 93. delete function now works
### Products not deleting in shopping bag
* Delete function not working, print statement in except Exception returns "POST /shopping_bag/delete/26/ HTTP/1.1" 500 0 'extra small'
### FIX: 
* Fixed typo in delete function in views removed [size] from line 63, 93. delete function now works
### Webhooks :
* Payment-intent not working: test webhook charge succeeded but internal server error stated there was an issue with a typo as follows....order = Order.object.create() whereas it should have been order = Order.objects.create().
### FIX: 
* Issue rectified, new endpoint set up and re-tested.
### Webhooks :
* User profile not updating on submit.
### FIX: 
* Syntax error in jinja templating, incorrect syntax for url ( missing })

# User Testing:

## Product deleting and size not showing on shopping bag page whe user updates a quantity

* This was a bug I had major issue trying to fix, checked source code from Boutique ado mainly focussing on the html rather than the python code.

### FIX: 
* Product increment/decrement button - created an if statement in the product increment/decrement html code and passed in value from the update_bag view.

```
{% if item.product.has_sizes %}
    <input type="hidden" name="product_size" value="{{ item.size }}">
{% endif %}
```

## Payments

* 500 error when card details submit, this may be down to an internal error with stripe as the text isnt found in any webhook handler
[Image](media/testing/payment-error.png)

## Bag pop-up

* CSS Amended but not carried over to heroku
[Image](media/testing/Bag-css-bug.png)








