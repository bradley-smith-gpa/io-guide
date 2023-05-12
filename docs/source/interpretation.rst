
##############
Interpretation
##############

*******************
Partial Derivatives
*******************

We commonly want to find out how the output of a sector will respond to given a change in 
final demand.

Fortunately, the hard work in finding the answers to such questions has already been done.

Recall the makeup for :math:`\mathbf{L}`:

.. math::

  \mathbf{L}
  =
  \begin{bmatrix}
  l_{11} & l_{12} \\
  l_{21} & l_{22}
  \end{bmatrix}

Each of the elements represents the partial derivative of a given output with respect to
a given sector. This result can be verified by multiplying out the matrices.

Each element links a unit increase in a given sector's final demand to a given sector's
change in output. For example, the term :math:`l_{21}` represents the change in :math:`y_2` (output for
sector :math:`2`) in response to a :math:`£1` increase in :math:`f_1` (final demand for
sector :math:`1`) *assuming all other variables are constant*.

.. danger::

  The increase of :math:`£1` is **exogenous**: an isolated change that is not
  explained by the model (used to represent an external hypothetical change).

  To add context, a :math:`£1` increase would be linked to an event such as increased consumption,
  investment, government spending and so on. Such events, however, do not happen in a "vacuum"
  and so one should be cautious not get "tunnel vision" with the usage of such partial derivatives.
  Economic events almost always occur with a tradeoff and so every effort must be made to consider
  and capture such effects in the model.

Since we have already worked out Leontief matrix, we know that this partial derivative
is the following:

.. math::

  l_{21} = \frac{\partial y_2}{\partial f_1}
  = \frac{a_{21}}{(1 - a_{11})(1 - a_{22}) - a_{12}a_{21}}


The advantage with the Lenotief matrix is that we can simply "read off" the matrix itself
to get these useful results (no need for any further rearranging etc.).

Inspecting the above result further, we can note the following:

* the larger :math:`a_{21}` is, the larger the increase in :math:`y_2`

  * the :math:`a_{21}` parameter controls how much sector :math:`1` needs from 
    sector :math:`2` in producing its output.

  * it is no surprise that, if sector :math:`1` relies heavily on sector :math:`2` inputs,
    sector :math:`2` will see a relatively larger boost in demand and therefore output
    for its good/service whenever the demand for sector :math:`1`'s good/service
    increases due to higher final demand for it.
