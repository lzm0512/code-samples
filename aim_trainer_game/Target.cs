using UnityEngine;

public class Target : MonoBehaviour
{
    public float lifetime = 3f;
    public Color hitColor = Color.red;

    private Renderer rend;
    private Color originalColor;
    private GameManager gameManager;

    void Start()
    {
        rend = GetComponent<Renderer>();
        originalColor = rend.material.color;
        Destroy(gameObject, lifetime);

        gameManager = Object.FindFirstObjectByType<GameManager>();
    }

    public void OnHit()
    {
        rend.material.color = hitColor;

        // score
        if (gameManager != null)
            gameManager.AddScore();

        Destroy(gameObject, 0.05f);
    }
}
