VAE_TOPOLOGIES = {
    "0.1": {
        "genome": "Mus_musculus_GRCm38_97",
        "hyper_parameters": {
                "latent_dim": (512, 64, 512),
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
                "latent_dim": (256, 128, 64, 128, 256),
                "l1_coef": 0.,
                "l2_coef": 0.,
                "dropout_rate": 0.,
                "batchnorm": True,
                "activation": "tanh",
                "init": "glorot_uniform",
                "output_layer": "nb_shared_disp"
        }
    },
    "0.3": {
        "genome": "Mus_musculus_GRCm38_97",
        "hyper_parameters": {
                "latent_dim": (512, 256, 128, 256, 512),
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
