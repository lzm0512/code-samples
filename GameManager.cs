using UnityEngine;
using TMPro;

public class GameManager : MonoBehaviour
{
    [Header("Spawning")]
    public GameObject targetPrefab;
    public Vector3 spawnArea = new Vector3(5, 3, 5);
    public float spawnInterval = 1f;

    [Header("UI")]
    public TMP_Text scoreText;
    private int score;

    private float timer;

    void Update()
    {
        timer += Time.deltaTime;
        if (timer >= spawnInterval)
        {
            SpawnTarget();
            timer = 0f;
        }
    }

    void SpawnTarget()
    {
        Vector3 pos = new Vector3(
            Random.Range(-spawnArea.x, spawnArea.x),
            Random.Range(1f, spawnArea.y),
            Random.Range(3f, spawnArea.z + 3)
        );
        Instantiate(targetPrefab, pos, Quaternion.identity);
    }

    public void AddScore()
    {
        score++;
        if (scoreText)
            scoreText.text = $"Score: {score}";
    }
}
