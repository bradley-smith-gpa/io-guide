#####
Annex
#####

************************
Matrix
************************

Collect all the output variables to one side :

.. math::

  (1- a_{11})y_1 - a_{12}y_2 &= f_1 \\
  a_{21}y_2 - (1 - a_{22})y_2 &= f_2

These equations are equivalent to the following equation written using matrices:

.. math::

  \begin{bmatrix}
  (1 - a_{11}) & -a_{12} \\
  -a_{21} & (1 - a_{22})
  \end{bmatrix}
  \cdot
  \begin{bmatrix}
  y_1 \\
  y_2
  \end{bmatrix}
  =
  \begin{bmatrix}
  f_1 \\
  f_2
  \end{bmatrix}
