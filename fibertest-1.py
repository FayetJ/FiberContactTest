import os
import random

from frontend import App

app = App.create("fitting")

model_root = "/tmp/objModels"
checkout_list = [
    "Models",
]
app.extra.sparse_clone(
    "https://github.com/FayetJ/FiberContactTest", model_root, checkout_list
)

bushing_path = os.path.join(model_root, checkout_list[0], "Bushing.obj")
tcp_end_path = os.path.join(model_root, checkout_list[0], "TcpEnd.obj")

V, E = app.mesh.line([0, 0.01, 0], [0.01, 15, 0], 960)
app.asset.add.rod("strand", V, E)

scene = app.scene.create()

N, scale = 11, 0.05
for i, j in np.ndindex((N, N)):
    x, y = scale * (i - N / 2), scale * (j - N / 2)
    obj = scene.add("strand").at(x, 1, y).jitter()
    (
        if i = 2:
            obj.pin().pull(5.0)

        obj.param.set("bend", 10)
        .set("contact-gap", 3e-3)
        .set("contact-offset", 3e-3)
        .set("friction", 0.05)
    )

opts = {"lookat": [0, 0.25, 0], "eyeup": 1.0, "fov": 4}

V, F = app.mesh.load_tri(bushing_path)
app.asset.add.tri("bushing_body", V, F)


bushing_body = scene.add("bushing_body").at(0,0,0)
pin = bushing_body.pin()
body_dir = os.path.join(codim_ipc_root, checkout_list[1])

scene.add.invisible.wall([0, -3, 0], [0, 1, 0])

scene = scene.build().report()
scene.preview(options={"pin": False})
