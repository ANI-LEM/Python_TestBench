import nidcpower

# Configure the session.

with nidcpower.Session(resource_name='PXI1Slot6', channels='0') as session:

    session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE

    session.commit()

    measurements = session.read_current_temperature()

    print(f"La temperature:{measurements}")
