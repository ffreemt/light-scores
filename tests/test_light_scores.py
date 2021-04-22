from light_scores import light_scores


def test_light_scores_sanity():
    _ = light_scores('x', 'y')
    assert _.mean() >= 0.0  # 0.0

    assert light_scores('x', 'x').mean() > -0.28  # -0.274
