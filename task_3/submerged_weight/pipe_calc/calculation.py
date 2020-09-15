from math import pi as PI


class Calculation:
    DEFAULT_INPUT_VALUES = {
        "pipe_od": 10.75,
        "pipe_wt": 0.5,
        "pipe_d": 490,
        "pipe_ca": 0.125,
        "coating_no": "1",
        "coating_desc": "FBE",
        "coating_t": 0.0118,
        "coating_d": 81.16,
        "contents_a_d": 0,
        "contents_w_d": 64,
        "contents_sw_d": 64.7,
    }

    NUMERIC_VALUE_KEYS = [
        "pipe_od",
        "pipe_wt",
        "pipe_d",
        "pipe_ca",
        "coating_t",
        "coating_d",
        "contents_a_d",
        "contents_w_d",
        "contents_sw_d",
    ]

    @classmethod
    def calculate(cls, input_values):
        """
        Will raise KeyError if all valus are not supplied
        Will raise ValueError if any required value is not valid
        """
        for key in cls.NUMERIC_VALUE_KEYS:
            input_values[key] = float(input_values[key])

        details_r1 = (input_values['pipe_od']-2*input_values['pipe_wt'])/2
        details_r2 = input_values['pipe_od']/2
        details_r3 = details_r2+input_values['coating_t']/2
        details_rt = details_r3*2

        dry_wt_pipe = PI*(details_r2**2-details_r1**2) / \
            144*input_values['pipe_d']
        dry_wt_coating = PI*(details_r3**2-details_r2**2) / \
            144*input_values['coating_d']
        dry_wt_contents = PI*details_r1**2/144*input_values['contents_a_d']
        dry_wt_total = sum([dry_wt_pipe, dry_wt_coating, dry_wt_contents])
        dry_buoyant_fc = PI*details_r3**2/144*input_values['contents_sw_d']

        summary_sub_wt = dry_wt_total-dry_buoyant_fc
        summary_sub_spec_gravity = dry_wt_total/dry_buoyant_fc

        output_values = {
            'details_r1': details_r1,
            'details_r2': details_r2,
            'details_r3': details_r3,
            'details_rt': details_rt,
            'dry_wt_pipe': dry_wt_pipe,
            'dry_wt_coating': dry_wt_coating,
            'dry_wt_contents': dry_wt_contents,
            'dry_wt_total': dry_wt_total,
            'dry_buoyant_fc': dry_buoyant_fc,
            'summary_sub_wt': summary_sub_wt,
            'summary_sub_spec_gravity': summary_sub_spec_gravity,
        }

        return output_values
