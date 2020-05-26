def test_HDL_analysis():
    from blood_analysis import HDL_analysis
    answer = HDL_analysis(70)
    expected = "Good"
    assert answer == expected
    
 