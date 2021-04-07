import nidcpower

# Configure the session.

with nidcpower.Session(resource_name='PXI1Slot6', channels='0') as session:
    session.measure_record_length = 1
    session.measure_record_length_is_finite = True
    session.measure_when = nidcpower.MeasureWhen.ON_DEMAND

    session.commit()
    print('Effective measurement rate: {0} S/s'.format(session.measure_record_delta_time / 1))

    samples_acquired = 0
    print('  #    Voltage    Current    Voltage_state')
    row_format = '{0:3d}:   {1:8.6f}   {2:8.6f}     {3:8.6f}   {4}'
    session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
    session.voltage_level_autorange = True
    session.voltage_limit_autorange = True
    # Pour envoyer le voltage au niveau de NI MAX
    session.current_limit = 0.9
    session.voltage_level = 5.0

    with session.initiate():
        # Boucle While, nous permettant de mesurer le voltage level en mode debugging au niveau de NI MAX Test Panel
        while samples_acquired < 20:
            session.output_enabled = True
            measurements = session.measure_multiple()
            Vmax_level = session.query_max_voltage_level(session.current_limit)

            V_out_STATE = session.query_output_state(nidcpower.OutputStates.CURRENT)

            for i in range(len(measurements)):
                print(row_format.format(i, measurements[i].voltage, measurements[i].current, Vmax_level, V_out_STATE))
