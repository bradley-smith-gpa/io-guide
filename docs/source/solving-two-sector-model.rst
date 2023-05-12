############################
Solving the Two-Sector Model
############################

************
Introduction
************

Recall the equations from the previous section:

.. math::

    y_1 &= \frac{z_{11}}{a_{11}} = \frac{z_{21}}{a_{21}} \\
    y_2 &= \frac{z_{12}}{a_{12}} = \frac{z_{22}}{a_{22}} \\
    d_1 &= z_{11} + z_{12} + f_1 \\
    d_2 &= z_{21} + z_{22} + f_2

To start solving these equations, let's use some basic supply and demand assumptions
to connect them together.

It is safely assumed that in equilibrium that supply is equal to demand. In other words,
:math:`d_1 = y_1` (e.g. the computer sector produces enough computers to satisfy demand).
This is a crucial step as it ties the ideas in the production function to
demand.

As a result, the above demand equations can be updated slightly:

.. math::

    y_1 &= z_{11} + z_{12} + f_1 \\
    y_2 &= z_{21} + z_{22} + f_2



*****************
Using Subsitution
*****************

First, we need to eliminate the demand values (the :math:`z` variables) from the above
equations.

Fortunately, we can use our other equations derived from the production function.

They can be rearranged so that we can an equation for each :math:`z` value:

.. math::

    z_{11} &= a_{11}y_1 \\
    z_{21} &= a_{21}y_1 \\
    z_{12} &= a_{12}y_2 \\
    z_{22} &= a_{22}y_2

Plugging each of the equations into our previous ones, leads to the following result:

.. math::

    y_1 &= a_{11}y_1 + a_{12}y_2 + f_1 \\
    y_2 &= a_{21}y_1 + a_{22}y_2 + f_2

We have managed to get a relationship between the outputs of each sector as well as
their final demand.

Now, we can rearrange the above so that we have equations for both :math:`y_1`
and :math:`y_2`:

.. math::

  y_1 &= \frac{1}{1- a_{11}}\left(a_{12}y_2 + f_1\right) \\
  y_2 &= \frac{1}{1- a_{22}}\left(a_{21}y_1 + f_2\right)

We can continue solving for :math:`y_1` by substituting :math:`y_2`:

.. math::

  y_1 &= \frac{1}{1- a_{11}}\left(a_{12}\left(\frac{1}{1- a_{22}}\right)\left(a_{21}y_1 + f_2\right) + f_1\right) \\
  y_1 &= \frac{a_{12}a_{21}}{(1- a_{11})(1- a_{22})}y_1 + \frac{a_{12}}{(1- a_{11})(1- a_{22})}f_2 + \frac{1}{1- a_{11}}f_1 \\

Next, we can collect :math:`y_1` to the left hand side:

.. math::

  (1- a_{11})(1- a_{22})y_1 &= a_{12}a_{21}y_1 + a_{12}f_2 + (1 - a_{22})f_1 \\
  (1- a_{11})(1- a_{22})y_1 - a_{12}a_{21}y_1 &= a_{12}f_2 + (1 - a_{22})f_1 \\
  y_1[(1- a_{11})(1- a_{22}) - a_{12}a_{21}] &= a_{12}f_2 + (1 - a_{22})f_1

We can divide through :math:`y_1`'s coefficient to get an equation for :math:`y_1`:

.. math::

  y_1 &= \frac{1}{(1- a_{11})(1- a_{22}) - a_{12}a_{21}} \bigg[ a_{12}f_2 + (1 - a_{22})f_1 \bigg] \\

We can alternatively express the right hand side so each final demand term has its own coefficient:

.. math::

  y_1 &= \left(\frac{1- a_{22}}{(1- a_{11})(1- a_{22}) - a_{12}a_{21}}\right)f_1 + \left(\frac{a_{12}}{(1- a_{11})(1- a_{22}) - a_{12}a_{21}}\right)f_2 \\

With :math:`y_1` known, the equivalent equation for :math:`y_2` can be found relatively easily:

.. math::

  y_2 &= \left(\frac{a_{21}}{(1- a_{11})(1- a_{22}) - a_{12}a_{21}}\right)f_1 + \left(\frac{1 - a_{11}}{(1- a_{11})(1- a_{22}) - a_{12}a_{21}}\right)f_2 \\

It is worth reminding ourselves that this is simply for a two-sector economy; in reality,
models are calculated over dozens (even hundreds) of sectors.

Of course, this method would be practically impossible to do as handling so many equations
would prove unwieldy. This is where matrix algebra comes in and is explored in next.


**************
Using Matrices
**************

The two-sector equations can be solved using matrices instead of the more labourious
method explained previously. The use of matrix algebra is the preferred method of solving
these systems of linear equations as it is faster and more compact to notate.

We can express our previous output equations in the form of matrices to "store" all those
terms in a grid-like fashion. As we will see, this type of arrangement allows us to perform
operations en-masse to efficiently reach a solution.

Let us define our key terms as matrices:

.. math::

  \mathbf{y} =
  \begin{bmatrix}
  y_1 \\
  y_2
  \end{bmatrix} \\

.. math::

  \mathbf{A} =
  \begin{bmatrix}
  a_{11} & a_{12} \\
  a_{21} & a_{22}
  \end{bmatrix} \\

.. math::

  \mathbf{f} =
  \begin{bmatrix}
  f_1 \\
  f_2
  \end{bmatrix} \\


Recall the following equations:

.. math::

    y_1 &= a_{11}y_1 + a_{12}y_2 + f_1 \\
    y_2 &= a_{21}y_1 + a_{22}y_2 + f_2

We are able to rewrite the above equations succinctly using our matrices:

.. math::

    \mathbf{y} = \mathbf{A}\mathbf{y} + \mathbf{f}

Moreover, we can collect the output terms to the left hand side:

.. math::

    \mathbf{y} - \mathbf{A}\mathbf{y} = \mathbf{f} \\
    (\mathbf{I} - \mathbf{A})\mathbf{y} = \mathbf{f}

After factoring out :math:`\mathbf{y}`, we can nullify the :math:`(\mathbf{I} - \mathbf{A})` term
on the left hand side by multiplying the entire equation by its inverse :math:`(\mathbf{I} - \mathbf{A})^{-1}`:

.. math::

    (\mathbf{I} - \mathbf{A})^{-1}(\mathbf{I} - \mathbf{A})\mathbf{y} &= (\mathbf{I} - \mathbf{A})^{-1}\mathbf{f} \\
    \mathbf{y} &= (\mathbf{I} - \mathbf{A})^{-1}\mathbf{f}

We can define the Leontief matrix :math:`\mathbf{L}` as being equal to :math:`(\mathbf{I} - \mathbf{A})^{-1}`:

.. math::

    \mathbf{y} = \mathbf{L}\mathbf{f}

It should be noted not to confuse the Leontief *matrix* :math:`\mathbf{L}` with the Leontief
production function from earlier. Moreover, this matrix should not be confused as
representing labour, which is often the case in economic models where the letter "L" is
used.

Now our task is to solve :math:`\mathbf{L}`.

First, let us work out :math:`(\mathbf{I} - \mathbf{A})`:

.. math::

    (\mathbf{I} - \mathbf{A}) =
    \begin{bmatrix}
    1 & 0 \\
    0 & 1
    \end{bmatrix}
    -
    \begin{bmatrix}
    a_{11} & a_{12} \\
    a_{21} & a_{22}
    \end{bmatrix} =
    \begin{bmatrix}
    (1 - a_{11}) & -a_{12} \\
    -a_{21} & (1 - a_{22})
    \end{bmatrix}

Now, let us work out the inverse of the above result :math:`(\mathbf{I} - \mathbf{A})^{-1}`
to get :math:`\mathbf{L}`.

As a refresher, recall the equation to work out the inverse of a generic matrix
:math:`\mathbf{M}`:

.. math::

  \mathbf{M}^{-1} = \frac{1}{\textnormal{det} (\mathbf{M})} \textnormal{adj}({\mathbf{M}})

We can see there are two components to be found:

* :math:`\textnormal{det} (\mathbf{M})` - the determinant of :math:`\mathbf{M}`
* :math:`\textnormal{adj} (\mathbf{M})` - the adjugate of :math:`\mathbf{M}`

If :math:`\mathbf{M}` is a :math:`2 \times 2` matrix with the following elements:

.. math::

  \mathbf{M} =
  \begin{bmatrix}
  a & b \\
  c & d
  \end{bmatrix}

Then its determinant and adjugate can be worked out and expressed with the following equation:

.. math::

  \mathbf{M}^{-1} =
  \frac{1}{ad - bc}
  \begin{bmatrix}
  d & -b \\
  -c & a
  \end{bmatrix}

Applying this equation to our example, we can work out the inverse of
:math:`(\mathbf{I} - \mathbf{A})`:

.. math::

  \mathbf{(\mathbf{I} - \mathbf{A})}^{-1} &=
  \begin{bmatrix}
  (1 - a_{11}) & -a_{12} \\
  -a_{21} & (1 - a_{22})
  \end{bmatrix}^{-1} \\
  &=
  \frac{1}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}}
  \begin{bmatrix}
  (1 - a_{22}) & a_{12} \\
  a_{21} & (1 - a_{11})
  \end{bmatrix} \\

.. math::

  \mathbf{L}
  =
  \begin{bmatrix}
  \frac{1 - a_{22}}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}} & \frac{a_{12}}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}} \\
  \frac{a_{21}}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}} &  \frac{1 - a_{11}}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}}
  \end{bmatrix}

Returning to our previous equation, we can now write it out in full now that we have :math:`\mathbf{L}`:

.. math::

  \begin{bmatrix}
    y_1 \\
    y_2
  \end{bmatrix}
  =
  \begin{bmatrix}
  \frac{1 - a_{22}}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}} & \frac{a_{12}}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}} \\
  \frac{a_{21}}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}} &  \frac{1 - a_{11}}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}}
  \end{bmatrix}
  \begin{bmatrix}
    f_1 \\
    f_2
  \end{bmatrix}

Since :math:`\mathbf{L}` is a little crowded with all those terms, each of these elements in
the matrix can be denoted by :math:`l` for brevity:

.. math::

  \begin{bmatrix}
    y_1 \\
    y_2
  \end{bmatrix}
  =
  \begin{bmatrix}
  l_{11} & l_{12} \\
  l_{21} & l_{22}
  \end{bmatrix}
  \begin{bmatrix}
    f_1 \\
    f_2
  \end{bmatrix}

Multiplying out these matrices will yield the solutions for :math:`y_1` and :math:`y_2`
(these of course are identical to what was worked out using substitution).
