import nidcpower

# Configure the session.

with nidcpower.Session(resource_name='PXI1Slot6', channels='0') as session:
    session.measure_when = nidcpower.MeasureWhen.ON_DEMAND
    types = nidcpower.MeasurementTypes.VOLTAGE

    session.commit()
    print('Effective measurement rate: {0} S/s'.format(session.measure_record_delta_time / 1))

    samples_acquired = 0
    print('  #    Voltage    Current    In Compliance')
    row_format = '{0:3d}:   {1:8.6f}   {2:8.6f}   {3}'
    with session.initiate():
        while samples_acquired < 1:
            measurements = session.measure(types)
            print(measurements)
