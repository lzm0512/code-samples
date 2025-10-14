using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerShoot : MonoBehaviour
{
    public Camera playerCamera;
    public float range = 100f;
    public LayerMask targetMask;

    public void OnFire(InputValue value)
    {
        if (!value.isPressed) return;

        Ray ray = playerCamera.ScreenPointToRay(new Vector3(Screen.width / 2, Screen.height / 2));
        if (Physics.Raycast(ray, out RaycastHit hit, range))

        {
            if (hit.collider.TryGetComponent(out Target target))
            {
                target.OnHit();
            }

        }
    }
}
