from chalice import Chalice, Response, BadRequestError

app = Chalice(app_name="chalice-demo")
app.debug = True


def water_pressure(h, rho=1025, g=9.81):
    """Calculate the water pressure head.

    Parameters
    ----------
    h : float : Water depth [m]
    rho : float : Fluid density [kg/m^3]
    g : float : Acceleration of gravitiy [m/s/s]

    Returns
    -------
    P_h : float : Pressure head [Pa]
    """
    return rho * g * h


@app.route("/")
def index():
    return Response(
        body="Calculate Water Pressure!",
        status_code=200,
        headers={"Content-Type": "text/plain"},
    )


@app.route("/{depth}")
def state_of_city(depth):

    try:
        h = float(depth)
    except ValueError:
        raise BadRequestError("Provide valid water depth.")

    P = water_pressure(h)
    # return {"pressure [Pa]": P}
    return Response(
        body=f"The water pressure at {h} m is {P} Pa.",
        status_code=200,
        headers={"Content-Type": "text/plain"},
    )

