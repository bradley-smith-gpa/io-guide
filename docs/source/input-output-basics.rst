###################
Input-Output Basics
###################

*************************************
Intersectoral and Intrasectoral Trade
*************************************


We can divide the economy into numerous sectors - such as dairy products, furniture,
veterinary services etc.

Intuitively, we know that there are goods/services flow between each sector in the economy.

For example, if we consider the food & beverage service sector - such as restaurants, it
is obvious that it purchases products from other sectors to provide the service - i.e. 
**intersectoral** trade.

Moreover, trade can occur within a given sector, which consitutues **intrasectoral** trade.
For example, a coffee shop that predominantly sells drink may want to branch out and
sell a few pastries to its customers. It can do so by purchasing them from the
local bakery, which belongs to the same food & beverage sector as the coffee shop itself.

Below are some examples of how a restaurant would interact with other sectors and why:

================================  =======================================  
Sectors                           Example Use      
================================  =======================================  
Meat Products                     Food served to customers
Soft Drinks                       Beverages served to customers
Electricity                       Power for appliances, lighting, heating
Real Estate Services              Renting the premises
Food & Beverage Service Sector    Prepared ingredients and dishes        
================================  =======================================

These flows are considered for a particular time period and can be thought of as 
a snapshot of the economy at a given point in time.

************
Final Demand
************

We have established that sectors demand goods/services from one another.
Of course, there are important areas within the economy that demand the
goods/services produced by the various sectors too. Broadly speaking, these areas are:

* consumers (also known as households)

* government

* foreign trade

These areas of demand are said to be **external** - or **exogenous** - to the sectoral
demand mentioned earlier.

**Final demand** is the sum of demand from these external (non-sectoral) entities.

Naturally, it is assumed that (at least for now) that the components of this final demand
are independent from sectoral demand. For example, government demand to build a new aircraft
carrier as part of defence spending is a largely political choice rather than being determined
by the day-to-day activity between various sectors.

This assumption is much weaker when it comes to 
households and it can be seen that, in more advanced versions of the input-output model,
this assumption is essentially discarded.
But for now, let us stick with this simple partitioning of demand as being sectoral and non-sectoral.

**********
Equations
**********

We can formulate what we have learnt so far into basic mathematical equations.

For example, consider a simple economy that consists of only two sectors:

#.  **Computer, electronic and optical products** 

#.  **Financial services**

For brevity, we will refer to each sector from now on as the **Computer** and the
**Finance** sector - just bear in mind that these sectors are quite broad and entail many
goods/services. The first production function we explore will only use the computer sector
to keep things simple.

=======
Supply
=======

We have established that the output of one sector uses goods/services from other sectors as
well as itself.

In economics, we use a **production function** to map the set of inputs to the
(maximum) output.

This output represents the supply of a given secttor.

These functions can be expressed as equations and therefore mathematically manipulated.

The exact makeup of such production functions vary wildly but for the input-output model, the
chosen type of production function will eventually be the **Leontief** production function.

Trivial Production Function
---------------------------

Although we know that many sectors exist in the economy, let us focus on a one-sector
economy to illustrate a trivial production function.

Let us denote the output of the computer sector output as :math:`y_1`.

We can define the following equation to describe the inputs need for the
**computer** sector output:

.. math::

  y_1 = \frac{z_{11}}{a_{11}}


In this basic economy, the computer sector demand for computers is represented as
:math:`z_{11}` (i.e. intrasectoral); this economy only consists of one type of sector trading that good/service
between itself.

Straight away we can observe that an increase in inputs :math:`z_{11}` will lead to higher
output :math:`y_{1}`: not at all surprising.

Exactly how much output will increase is determined by the term :math:`a_{11}` which is
known as a **technical coefficient**.

Technical coefficients are a (very basic) way of relating a given input to the final output;
it controls the magnitude of the impact a change in a given input makes.
The term "technical" is derived from the fact that these parameters represent the technology
required to produce output.

We can work out what our technical coefficient :math:`a_{11}` is if we have the right data.

For this example, we can fill in some imaginary values to work out :math:`a_{11}`.

Suppose that it is observed that the computer company produced :math:`100` computers last
year. To acheive this, it is also known that the computer firm bought :math:`50` laptops
for its employees to enable them to acheive this output. Using extremely simple
arithmetic, we can work out :math:`a_{11}`:

.. math::

  a_{11} = \frac{z_{11}}{y_1} = \frac{50}{100} = 0.5

Now that we know the value of our technical coefficient, we can rewrite our inital equation:


.. math::

  y_1 = \frac{z_{11}}{0.5}

Armed with our production function, we can now work out what the output would be for any 
arbitrary number of inputs. We would know that - if the number of laptops as inputs
increased to :math:`75` - then output would increase to :math:`150`.

Leontief Production Function
----------------------------

Of course, the production function above is trivial and we want to expand our production
function to incorporate inputs from other sectors. As we will see, the introduction of
another sector leads to some interesting complexity. To acheive this, we will use
a Leontief production function.

First, let us denote the output of each sector with the expression :math:`y`:

#.  computer sector output (:math:`y_1`)

#.  finance sector output (:math:`y_2`)


Second, let us define the notation to indicate demand between all sectors:

* intrasectoral

  * computer sector demand for computers (:math:`z_{11}`)

    * flow of goods/services from sector :math:`1` to sector :math:`1`

  * finance sector demand for finacial services (:math:`z_{22}`)

    * flow of goods/services from sector :math:`2` to sector :math:`2`

* intersectoral

  * computer sector demand for finance services (:math:`z_{21}`)

    * flow of goods/services from sector :math:`2` to sector :math:`1`

  * finance sector demand for computers (:math:`z_{12}`)

    * flow of goods/services from sector :math:`1` to sector :math:`2`

From the breakdown above, it is apparent that we have 4 demand variables to keep track of:
clearly, this is a step up from our previous production function in terms of complexity.

There is also an important assumption in the relationship between the inputs.

A Leontief production function assumes that output is determined by the lowest ratio of input
to its technical coefficient. At first, this does not appear to make much sense,
but observe the Leontief production function below before we revisit this crucial concept:

.. math::

   y_1 = \min\left(\frac{z_{11}}{a_{11}}, \frac{z_{21}}{a_{21}}\right)

Referring to the demand expressions defined above, we can see the output of computers
produced :math:`y_1` requires inputs from the computer sector itself :math:`z_{11}`
(as seen previously) and the finance sector :math:`z_{21}`.

* for :math:`z_{11}`, an example would be that a company that manufactures computers may purchase
  laptops for its workers (which were bought from a different computer company).

* for :math:`z_{21}`, an example would be the computer hiring accountants for services
  to prepare its accounts.

The terms :math:`a_{11}` and :math:`a_{21}` are the technical coefficients we saw
previously.


The :math:`\min` operator indicates to pick the smaller (towards the left of the number line)
of the two values. It relates to the assumption stated above and can be thought of as
indicating how inputs need to be used in fixed proportions.

Let us fill in the above equation with techinical coefficients to see the mechanics of this:

.. math::

   y_1 = \min\left(\frac{z_{11}}{0.5}, \frac{z_{21}}{5}\right)

Furthermore, let us assume some input values aswell:

* let :math:`z_{11}` represent the number of laptops required with a value of say :math:`50`.

* let :math:`z_{21}` represent the hours required by accountants :math:`500`.

Evaluating our formula with these values, we can calculate the output:

.. math::

  y_1 = \min\left(\frac{50}{0.5}, \frac{500}{5}\right)
      = \min\left(100, 100\right)
      = 100
  
This somewhat contrived example yields a value of :math:`100` under both inputs.
Obviously, the minimum between two of the same number is just that number.
In this case, then we can determine that...

.. math::

   y_1 = \frac{z_{11}}{a_{11}}

...or...

.. math::

   y_1 = \frac{z_{21}}{a_{21}}

We can use either expression here since they are both equal: these "shortcut"
equations will be used later on.

Now, consider the output if one of the inputs, say the hours of hired accountants used, increased
significantly to say :math:`2,000`:

.. math::

  y_1 = \min\left(\frac{50}{0.5}, \frac{2,000}{5}\right)
      = \min\left(100, 400\right)
      = 100

It can be seen that we have arrived at exactly the same answer as before of :math:`100`
thanks to our of :math:`\min` operator.

The economic logic behind such a result is this:

* If you are the computer company, you need to have both laptops for your workers and
  accountants to do your books in a given ratio.

* If you hire many accountants (like in the example above), this is not going to
  increase output assuming that your other input(s) have not increased as well.

* In other words, you can hire as many bean counters you want, but if
  you do not equip your workers with enough laptops, the computer company is not going to
  produce any more computers.

A similar story could be constructed for the other case: perhaps it is useless to
provide more laptops for workers if there is not a commensurate increase in accountants
who would be legally required to fulfill the bookkeeping requirements
of a higher-output (i.e. larger) company.

Given this, a rational company would not purchase an "excess" of one input as that would
be a total waste. Therefore, it is assumed that companies - and therefore the sector
as a whole would - operate on the basis explored in the situation above where the
input-technical-coefficient ratios are the same. This is in an important assumption as
we can use those "shortcut" equations and side-step having to use the :math:`\min` operator
later on.

To reinforce our knowledge once more, we can neatly summarise the Leontief production
function as the following for both sectors if :math:`y_2` represents finance sector output:

.. math::

  y_1 = \frac{z_{11}}{a_{11}} = \frac{z_{21}}{a_{21}}

  \\

  y_2 = \frac{z_{12}}{a_{12}} = \frac{z_{22}}{a_{22}}

======
Demand
======

We can formulate an equation to show the composition of demand for a given sector's
good/service.

We can need to supplement, however, our variables with the final demand mentioned earlier.
Therefore, we define the following expressions:

* final demand for computers (:math:`f_1`)

* final demand for financial services (:math:`f_2`)

Applying our knowledge so far, we can define the following equation to describe the
demand for **computers**:

.. math::

  d_1 = z_{11} + z_{12} + f_1

The demand for computers is denoted as :math:`d_1` and is dervied from the:

* computer sector itself :math:`z_{11}`.

* finance sector :math:`z_{12}`.

* final demand of computers :math:`f_1` (from consumers, government and foreign trade).

Similarly, we can write the same equation for the finance sector:

.. math::

  d_2 = z_{21} + z_{22} + f_2

===============
Interdependency
===============

So far we have determined the supply and demand equations listed below:

.. math::

   \begin{eqnarray}
      y_1 & = & \frac{z_{11}}{a_{11}} = \frac{z_{21}}{a_{21}} \\
      y_2 & = & \frac{z_{12}}{a_{12}} = \frac{z_{22}}{a_{22}} \\
      d_1 & = & z_{11} + z_{12} + f_1 \\
      d_2 & = & z_{21} + z_{22} + f_2
   \end{eqnarray}

Of course, we want to measure the effect of say final demand for computers :math:`f_1` on
say the the supply of computers :math:`y_1`. Just from looking at the equations, it is
not quite clear what the answer is. This is mainly due to the fact that all these 
equations are interlinked - i.e. these sectors are interdependent. In order to answer such
questions, we need to solve this system of equations.

We will do that in the next section but, for now, it is important to realise why setting
out all these equations is useful; it allows us to trace effects through our simple
modelled economy in an objective manner. Without such a model, it is essentially
impractical to determine the effects within it given that there are many "moving parts" to
keep track of. It is for such reasons that the input-output is intended to solve.
