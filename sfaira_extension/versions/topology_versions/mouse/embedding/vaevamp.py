VAEVAMP_TOPOLOGIES = {
    "0.1": {
        "genome": "Mus_musculus_GRCm38_97",
        "hyper_parameters": {
            "latent_dim": (32, 32),
            "l1_coef": 0.,
            "l2_coef": 0.,
            "dropout_rate": 0.,
            "batchnorm": True,
            "activation": "tanh",
            "init": "glorot_uniform",
            "output_layer": "nb_shared_disp"
        }
    },
    "0.2": {
        "genome": "Mus_musculus_GRCm38_97",
        "hyper_parameters": {
            "latent_dim": (64, 64),
            "l1_coef": 0.,
            "l2_coef": 0.,
            "dropout_rate": 0.,
            "batchnorm": True,
            "activation": "tanh",
            "init": "glorot_uniform",
            "output_layer": "nb_shared_disp"
        }
    }
}
